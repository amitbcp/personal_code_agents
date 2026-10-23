import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../skills/archify');
const {startDeliveryUpdateCheck} = await import(path.join(root,'bin/delivery-update.mjs'));
const update = await startDeliveryUpdateCheck({env: {}, checkerPath: '/nonexistent/checker.mjs'});
assert.equal(update.reason,'disabled');
const work = fs.mkdtempSync(path.join(os.tmpdir(),'archify-adaptation-'));
try {
 const run = (...args) => spawnSync(process.execPath,[path.join(root,'bin/archify.mjs'),...args],{cwd:work,encoding:'utf8',timeout:30000});
 const out=path.join(work,'diagram.html');
 const good=run('deliver','architecture',path.join(root,'examples/web-app.architecture.json'),out,'--quality','showcase','--json');
 assert.equal(good.status,0,good.stderr||good.stdout);
 const receipt=JSON.parse(good.stdout);assert.equal(receipt.ok,true);assert.equal(receipt.update.reason,'disabled');
 const checked=run('check',out,'--require-provenance');assert.equal(checked.status,0,checked.stderr);assert.equal(JSON.parse(checked.stdout).provenance,'current');
 const before=fs.readFileSync(out);
 const bad=path.join(work,'bad.json');fs.writeFileSync(bad,'{"diagram_type":"architecture"}');
 const rejected=run('deliver','architecture',bad,out,'--quality','showcase','--json');
 assert.notEqual(rejected.status,0);assert.deepEqual(fs.readFileSync(out),before);
 console.log('PASS: default update disabled; standalone deliver/check; invalid candidate rejected; previous artifact preserved.');
} finally {fs.rmSync(work,{recursive:true,force:true});}
