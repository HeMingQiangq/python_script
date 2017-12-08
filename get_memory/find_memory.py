#--**coding:utf-8**--


import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

# Iterate processes
#processLines:系统现有的进程，是个列表
processLines = ps.split('\n')
#print "processLines:",processLines
sep = re.compile('[\s]+')
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    #遍历出processLines列表中的进程名
    rowText = processLines[row].strip()
    #print "rowText:",rowText
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
print "vmLines:",vmLines
sep = re.compile(':[\s]+')
vmStats = {}
for row in range(1,len(vmLines)-2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096

'''
wired是不能通过操作系统调度来协调的内存，用了多少就是多少；
active是表示当前系统的软件等使用所占用的内存，是有效的数据
inactive表示内存数据曾经被使用过，但最近没有使用，有效的数据
free表示数据无效，也就是随时可以被操作系统调度用来做别的事情

'''
print vmStats
print "\n\t"
print '系统核心内存:\t\t\t\t\t%d MB' % ( vmStats["Pages wired down"]/1024/1024 )
print '正被使用的内存数据:\t\t\t%d MB' % ( vmStats["Pages active"]/1024/1024 )
print '数据存在，但未被使用的内存:\t\t%d MB' % ( vmStats["Pages inactive"]/1024/1024 )
print '剩余可用内存:\t\t\t\t\t%d MB' % ( vmStats["Pages free"]/1024/1024 )
print "\n\t"
print 'Real Mem Total (ps):\t%.3f MB' % ( rssTotal/1024/1024 )
print 'Wired Memory:\t\t\t%d MB' % ( vmStats["Pages wired down"]/1024/1024 )
print 'Active Memory:\t\t\t%d MB' % ( vmStats["Pages active"]/1024/1024 )
print 'Inactive Memory:\t\t%d MB' % ( vmStats["Pages inactive"]/1024/1024 )
print 'Free Memory:\t\t\t%d MB' % ( vmStats["Pages free"]/1024/1024 )
print 'Real Mem Total (ps):\t%.3f MB' % ( rssTotal/1024/1024 )