"""Execute the RUM example without a browser/network; verify its privacy boundary."""
import json
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]

@unittest.skipUnless(shutil.which('node'), 'Node required to execute JavaScript example')
class RumExampleTests(unittest.TestCase):
    def test_route_allowlist_omits_unapproved_identifiers(self):
        source = (ROOT/'skills/web-performance/references/RUM.md').read_text().split('```javascript\n',1)[1].split('```',1)[0]
        source = '\n'.join(line for line in source.splitlines() if not line.startswith('import '))
        harness = '''
const sent=[];
const window={APP_RELEASE:'fixture'};
const navigator={sendBeacon:(url,body)=>{sent.push(JSON.parse(body));return true;}};
const onCLS=()=>{}, onINP=()=>{}, onLCP=()=>{};
'''+source+'''
for(const value of ['home','customer-order-detail','/customers/alice@example.test/orders/123',undefined]) {
 window.APP_ROUTE_NAME=value;
 sendToRum({name:'LCP',value:10,rating:'good',id:'fixture',navigationType:'navigate'});
}
console.log(JSON.stringify(sent));
'''
        result=subprocess.run(['node','-e',harness],check=True,capture_output=True,text=True)
        sent=json.loads(result.stdout)
        self.assertEqual([x.get('route') for x in sent],['home','customer-order-detail',None,None])
        self.assertTrue(all('path' not in x for x in sent))
        self.assertNotIn('alice@example.test',result.stdout)

class OracleExampleTests(unittest.TestCase):
    def test_algebraic_laws_do_not_replace_addition_contract(self):
        from itertools import product
        wrong_add=lambda a,b:a^b
        values=range(-5,6)
        self.assertTrue(all(wrong_add(a,b)==wrong_add(b,a) for a,b in product(values,repeat=2)))
        self.assertTrue(all(wrong_add(wrong_add(a,b),c)==wrong_add(a,wrong_add(b,c)) for a,b,c in product(values,repeat=3)))
        self.assertTrue(all(wrong_add(a,0)==a for a in values))
        self.assertNotEqual(wrong_add(1,1),1+1)

if __name__=='__main__':unittest.main()
