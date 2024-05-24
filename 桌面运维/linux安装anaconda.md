# linux 安装 anaconda

一 平台:

平台:CentOS Linux release 7.5.1804 (Core)

Anacoda版本:CentOS Linux release 7.5.1804 (Core)

二、执行如下步骤：

```undefined
yum install -y bzip2
```

bash Anaconda3-2022.05-Linux-x86_64.sh

三、配置环境（安装如上步骤，会自动生成如下脚本，如果没有自动生成，请参考配置）

cat /root/.bashrc
# .bashrc

```
# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions

if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# >>> conda initialize >>>

# !! Contents within this block are managed by 'conda init' !!

__conda_setup="$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/root/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/root/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/root/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup

# <<< conda initialize <<<
```

四、验证 

```
cat /root/.bashrc
# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/root/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/root/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/root/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

