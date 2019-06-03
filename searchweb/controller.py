## written by Mroylib
import re
import asyncio
from concurrent.futures.thread import  ThreadPoolExecutor
from mroylib.servers.tornado import Base, Manifest,check

def mark(text, key):
    w = re.compile(r'(%s)'%key)
    return w.sub('<code>%s</code>' % key, text)

Pockets = ThreadPoolExecutor(max_workers=12)

async def run_command(*args):
    
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args,
        # stdout must a pipe to be accessible as process.stdout
        stderr=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE)
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode != 0:
        result = stderr.decode().strip()
        print('Failed:', args, '(pid = ' + str(process.pid) + ')')
    else:
        result = stdout.decode().strip()
    return result

async def search(key, root):
    d = {}
    lines = await run_command("ag", key, root)
    lines = lines.split("\n")
    for l in lines:
        f,line,v = l.split(":",2)
        va = d.get(f,"")
        va += v +"\n"
        d[f] = va
    return d


TP = {
    'py':'python',
    'rb':'ruby',
    'sh':'bash',
    'json':'json',
    'js':'javascript'
}
class Index(Base):
    @check
    async def get(self):
        return  {"datas":[]}
        # test = """UIModules are a feature of the tornado.web.RequestHandler class (and specifically its render method) and will not work when the template system is used on its own in other contexts.ado.web.RequestHandler class (and specifically its render method) and will not work when the template system is used on its own in other contexts.ado.web.RequestHandler class (and specifically its render method) and will not work when the template system is used on its own in other contexts.ado.web.RequestHandler class (and specifically its render method) and will not work when the template system is used on its own in other contexts."""
        # return {"datas":[
        #     {"link":"/", "text":test},
        #     {"link":"/", "text": mark(test,'Request')},
        # ]}

    @check
    async def post(self, name):
        print(self.settings['ui_modules'])
        TextModule = self.settings['ui_modules']['Textcard']
        t= TextModule(self)
        res_dict = await search(name, self.settings['search-root'])
        res = []
        # if len(res_dict) > 20000:
        #     _p = 0
        #     for n,i in enumerate(res_dict):
        #         if n % 20 == 0:
        #             _p += 1
        #         if _p == page:
        #             tp = i.split(".")[-1]
        #             tp = TP.get(tp, tp)
        #             res.append(t.render(link='/' + i,tp=tp, text=mark(res_dict[i], name), title=i).decode())
        # else:
        for i in res_dict:
            tp = i.split(".")[-1]
            tp = TP.get(tp, tp)
            res.append(t.render(link='/' + i,tp=tp, text=mark(res_dict[i], name), title=i).decode())
        return  {"datas":res, 'page':0}
