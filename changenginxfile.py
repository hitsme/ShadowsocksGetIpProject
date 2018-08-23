import io
with io.open('config.php','r',encoding='utf-8') as f:
           lines=f.readlines()
with io.open("config.php","w",encoding="utf-8") as f_w:
           for line in lines:
               if "ip" in line:
                   line=line.replace("ip","ip123")
                   f_w.write(line)
               else:
                   f_w.write(line)