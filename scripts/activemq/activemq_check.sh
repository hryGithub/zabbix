#!/bin/bash

HOST=192.168.9.149
PORT=8161
USER=admin
PASSWORD=admin

#obtain queue's Pending,Consumers,Enqueued,Dequeued
function Queue()
{
  Count=$(curl -u"$USER":"$PASSWORD" http://$HOST:$PORT/admin/queues.jsp 2> /dev/null |grep -A 5 "^$1"|grep -oP '\d+');
  #echo $Count
  Pending=$(echo $Count |awk '{print $1}');
  #echo $Count
  Consumers=$(echo $Count |awk '{print $2}');
  Enqueued=$(echo $Count |awk '{print $3}');
  Dequeued=$(echo $Count |awk '{print $4}');
  #EndeltaDn=$(($Enqueued - $Dequeued))
  #echo '-------------'
  #echo -e "$Pending\n$Consumers\n$Enqueued\n$Dequeued";
  #echo "$2"
  if [ "$2" = '' ];then
     exit
  fi
  if [ "$2" = 'Pending' ];then
    echo $Pending
  elif [ "$2" = 'Consumers' ];then
    echo $Consumers
  elif [ "$2" = 'Enqueued' ];then
    echo $Enqueued
  #elif [ "$2" = 'EndeltaDn' ];then
  #  echo $EndeltaDn
  else
    echo $Dequeued
  fi
}

#call function and input queue_name queue_type
Queue $1 $2 