#!/bin/bash

killZombie() {
YESTERDAY_1=`date -d '-1 day' +%b%d`
YESTERDAY_2=`date -d '-2 day' +%b%d`
ps -ef|grep fglrun|grep -v 'grep'|grep -E 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'|grep -v "$YESTERDAY_1"|grep -v "$YESTERDAY_2"|awk '{print $2}'|xargs kill -9
}

cleanBigFile(){
BIGFILESIZE=204800
TARGETDIR=/ut
SAVEDAY=5
LASTROW=50000
cd $TARGETDIR
find "$TARGETDIR" -xdev -ctime +"$SAVEDAY" -name "*" -exec rm -f {} \;

find $TARGETDIR -name *.*  > /tmp/list

for i in `cat /tmp/list`
do
  filesize=`du $i|awk '{print $1}'`
  if [[ "$filesize" -gt "$BIGFILESIZE" ]] ; then
    tail -n $LASTROW $i > "$i".bak
    cat /dev/null > $i
  fi
done
}

checkWeb(){
topprd_status=`ps -ef|grep xcf|grep -v "grep"|grep -w "topprd.xcf"|wc -l`
topprd_ws_status=`ps -ef|grep xcf|grep -v "grep"|grep -w "topprd-ws.xcf"|wc -l`
if [[ "$topprd_status" != "1" ]] ; then
  echo "`date` restart gas_topprd" >> /u3/log/guardBaseService.log
  systemctl restart gas_topprd
fi
if [[ "$topprd_ws_status" != "1" ]] ; then
  echo "`date` restart gas_topprd_ws" >> /u3/log/guardBaseService.log
  systemctl restart gas_topprd_ws
fi
}

#!/bin/bash
a1()
{ls}
a2()
{ll}
