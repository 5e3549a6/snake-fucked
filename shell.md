这里主要总结下，在 Python 代码脚本里，涉及到调用 Shell 脚本、终端命令行、其它 Python 脚本的场景.

## 1. 方法1 - os.system()

**os.system()** - 只返回状态码，执行结果会输出到stdout，即输出到终端. **仅在 Linux 中有效**.

用法：

```python
import os

# 不传递参数
os.system(cmd) # cmd 即为Linux 终端命令行指令
               # 返回命令执行的状态值
               # 输出数字为 0，表示正确执行；
               # 输出数字非 0，表示错误执行
            
# 传递一个参数
os.system("shell command argus %s" % argus1)

# 传递两个及以上参数
os.system("shell command argus %s %s" % (argus1, argus2)
```

如：

```python
import os

# 不传递参数
os.system("ls")    # 显示文件夹文件，不包含隐藏文件
os.system("ls -a") # 显示文件夹所有文件，包含隐藏文件
os.system("pwd")   # 获取当前目录
os.system("top")   # 显示进程情况，退出需要输入 'q'.

# 传递一个参数
os.system("python test.py -i %s" %inputparam)

# 传递两个及以上参数
os.system("python test.py -i %s -b %s" % (inputparam1, inputparam2))
```

**注：`os.system(cmd)` 不能执行交互式命令，如 `ssh root@ip` 需要输入密码的终端命令**.

**Python 字符格式化：**

```protobuf
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数(基底写为e)
%E    指数(基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"
```

>   参考：[os.system如何传参](https://blog.csdn.net/njafei/article/details/72764990)

## 2. 方法二 - os.popen()

**os.popen()** - 用于从一个命令打开一个管道，返回结果是一个连接管道的文件对象，该文件对象的操作方法同 **open()**，可以从该文件对象中读取返回结果. 如果执行成功，不会返回状态码，如果执行失败，则会将错误信息输出到stdout，并返回一个空字符串. **在Unix，Windows中有效**.

用法：

```python
import os

os.popen(cmd, mode, bufsize)
# cmd - 使用的命令。
# mode - 模式权限可以是 'r'(默认) 或 'w'.
# bufsize - 指明文件需要的缓冲大小：
#            0-无缓冲；1-行缓冲；
#            其它正值表示使用参数大小的缓冲（大概值，以字节为单位）
#            负的bufsize意味着使用系统的默认值.
#           一般来说，对于tty设备，它是行缓冲；
#            对于其它文件，它是全缓冲. 如果没有改参数，使用系统的默认值.
# 返回一个文件描述符号为 fd 的打开的文件对象.
```

如：

```python
import os

files = os.popen("ls").readlines() # 文件夹内所有文件的列表.
```

**注:**  `os.popen()`在大多数场景都是挺好用，但需要注意：

[1] -  在需要读取命令执行结果时，避免在命令无法退出或进入交互模式的场景应用 `os.popen()`;

[2] - `os.popen()`无法满足需求时，可以考虑`subprocess.Popen()`.

>   参考：[关于os.popen你可能不知道的](https://blog.51cto.com/2681882/2317053)

## 3. 方法三 - subprocess 模块

>   [docs - subprocess](https://docs.python.org/3.6/library/subprocess.html)

**subprocess 模块**是 Python 2.4 版本开始引入的模块，主要用来取代 一些旧的模块方法，如`os.system`、`os.spawn`、`os.popen`、`commands.*`等.

**subprocess** 通过子进程来执行外部指令，并通过 **input/output/error** 管道，获取子进程的执行的返回信息.

### 3.1. subprocess.Popen()

用法：

```python
class subprocess.Popen(args, 
                       bufsize=-1, 
                       executable=None, 
                       stdin=None, 
                       stdout=None, 
                       stderr=None, 
                       preexec_fn=None, 
                       close_fds=True, 
                       shell=False, 
                       cwd=None, 
                       env=None, 
                       universal_newlines=False, 
                       startupinfo=None, 
                       creationflags=0, 
                       restore_signals=True, 
                       start_new_session=False, 
                       pass_fds=(), 
                       *, 
                       encoding=None, 
                       errors=None)
```

>   参考: [python中的subprocess.Popen（）使用](https://www.cnblogs.com/Security-Darren/p/4733368.html)

参考: [Python多进程（1）——subprocess与Popen()](https://www.cnblogs.com/Security-Darren/p/4733368.html)

**参数说明：**

[![image](https://www.aiuai.cn/uploads/2019/04/440150960.jpg)](https://www.aiuai.cn/uploads/2019/04/440150960.jpg)

[image](https://www.aiuai.cn/uploads/2019/04/440150960.jpg)



[1] - **args 参数：** 要执行的命令或可执行文件的路径. 一个由字符串组成的序列（通常是列表），列表的第一个元素是可执行程序的路径，剩下的是传给这个程序的参数，如果没有要传给这个程序的参数，args 参数可以仅仅是一个字符串。

[2] - **bufsize**：控制 *stdin*, *stdout*, *stderr* 等参数指定的文件的缓冲，和打开文件的 `open()` 函数中的参数 *bufsize* 含义相同.

[3] - **executable**：如果这个参数不是 None，将替代参数 args 作为可执行程序；

[4] - **stdin**：指定子进程的标准输入；

[5] - **stdout**：指定子进程的标准输出；

[6] - **stderr**：指定子进程的标准错误输出；

对于 *stdin, stdout* 和 *stderr* 而言，如果它们是 None（默认情况），那么子进程使用和父进程相同的标准流文件. 父进程如果想要和子进程通过 communicate() 方法通信，对应的参数必须是 subprocess.PIPE；*stdin, stdout* 和 *stderr* 也可以是已经打开的 file 对象，前提是以合理的方式打开，比如 *stdin* 对应的文件必须要可读等. 

[7] - **preexec_fn**：默认是None，否则必须是一个函数或者可调用对象，在子进程中首先执行这个函数，然后再去执行为子进程指定的程序或Shell.

[8] - **close_fds**：布尔型变量，为 True 时，在子进程执行前强制关闭所有除 stdin，stdout和stderr外的文件；

[9] - **shell**：布尔型变量，明确要求使用shell运行程序，与参数 executable 一同指定子进程运行在什么 Shell 中 —— 如果executable=None 而 shell=True，则使用  /bin/sh 来执行 args 指定的程序；也就是说，Python首先起一个shell，再用这个shell来解释指定运行的命令.

[10] - **cwd**：代表路径的字符串，指定子进程运行的工作目录，要求这个目录必须存在；

[11] - **env**：字典，键和值都是为子进程定义环境变量的字符串；

[12] - **universal_newline**：布尔型变量，为 True 时，*stdout* 和 *stderr* 以通用换行（universal newline）模式打开，

[13] - **startupinfo**：见下一个参数；

[14] - **creationfalgs**：最后这两个参数是Windows中才有的参数，传递给Win32的CreateProcess API调用.

**例1：**

```python
import subprocess

p = subprocess.Popen('ls -l', shell=True)

p.returncode
p.wait() # 0
p.pid # 子进程的 PID
p.returncode # 子进程的返回状态.
             #  None —— 子进程尚未结束；
             #  ==0 —— 子进程正常退出；
             #  > 0—— 子进程异常退出，returncode对应于出错码；
             #  < 0—— 子进程被信号杀掉了.
p.stdin
p.stdout
p.stderr
```

**例2：**

>   From: [Python subprocess.Popen 实时输出 stdout（正确管道写法）](https://blog.csdn.net/u012206617/article/details/84560895)

```python
import sbuprocess

proc = subprocess.Popen(cmd, 
                        shell=True, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
try:
    while True:
        buff = proc.stdout.readline()
        print(buff)
        if buff == '' and proc.poll() != None:
            break
        else:
            .....
except Exception:
    data["status"] = -1
finally:
    return data
```

>   From: [python的subprocess模块](https://www.cnblogs.com/breezey/p/6673901.html)

**subprocess.Popen()** - 在一些复杂场景中，需要将一个进程的执行输出作为另一个进程的输入. 在另一些场景中，需要先进入到某个输入环境，然后再执行一系列的指令等. 这个时候就需要使用到**suprocess.Popen()方法**，该方法有以下参数：

[1] - **args：**shell命令，可以是字符串，或者序列类型，如list,tuple.

[2] - **bufsize：**缓冲区大小，可不用关心

[3] - **stdin, stdout, stderr：**分别表示程序的标准输入，标准输出及标准错误

[4] - **shell：** 与 **subprocess.call()** 中相同.

[5] - **cwd：**用于设置子进程的当前目录

[6] - **env：**用于指定子进程的环境变量. 如果env=None，则默认从父进程继承环境变量.

[7] - **universal_newlines：**不同系统的的换行符不同，当该参数设定为true时，则表示使用n作为换行符.

**例如1：**

```python
status = subprocess.Popen('mkdir subprocesstest',shell=True,cwd='/root')
```

**例如2：**

```python
import subprocess

obj = subprocess.Popen(["python"], 
                       stdin=subprocess.PIPE, 
                       stdout=subprocess.PIPE, 
                       stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n')
obj.stdin.write('print 2 \n')
obj.stdin.write('print 3 \n')
obj.stdin.write('print 4 \n')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print cmd_out
print cmd_error

# 或
import subprocess

obj = subprocess.Popen(["python"], 
                       stdin=subprocess.PIPE, 
                       stdout=subprocess.PIPE, 
                       stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n')
obj.stdin.write('print 2 \n')
obj.stdin.write('print 3 \n')
obj.stdin.write('print 4 \n')

out_error_list = obj.communicate()
print out_error_list
```

**例如3：**

```python
import subprocess

# 将一个子进程的输出，作为另一个子进程的输入：
child1 = subprocess.Popen(["cat","/etc/passwd"], 
                          stdout=subprocess.PIPE)
child2 = subprocess.Popen(["grep","0:0"],
                          stdin=child1.stdout, 
                          stdout=subprocess.PIPE)
out = child2.communicate()
```

**例如4：**

```python
import subprocess

child = subprocess.Popen('sleep 60',
                         shell=True,
                         stdout=subprocess.PIPE)
child.poll()        # 检查子进程状态
child.kill()        # 终止子进程
child.send_signal() # 向子进程发送信号
child.terminate()   # 终止子进程
```

### 3.2. subprocess.call()

**subprocess.call()** - 执行命令，并返回执行状态. 其中shell参数为False时，命令需要通过列表的方式传入；当shell为True时，可直接传入命令.

例如：

```python
import subprocess

status1 = subprocess.call(['df','-hT'],shell=False)
status2 = subprocess.call('df -hT',    shell=True)
print(status1) # 0
print(status2) # 0
```

### 3.3. subprocess.check_call()

**subprocess.check_call()** - 用法与**subprocess.call()**类似，区别是，**当返回值不为0时，直接抛出异常**.

例如：

```python
import subprocess

status2 = subprocess.check_call('df -hT',    shell=True)
print(status2) # 0

status1 = subprocess.check_call('dfdadas',    shell=True) #出错，异常.
```

### 3.4. subprocess.check_output()

**subprocess.check_output()** - 用法与**subprocess.call()**、**subprocess.check_call()**类似，区别是，××如果当返回值为0时，直接返回输出结果，如果返回值不为0，直接抛出异常**.  

**subprocess.check_output() 仅在python3.x中才有**.