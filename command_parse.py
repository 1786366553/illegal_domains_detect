

import sys,getopt

def command_parse(argvs):

    start_index = total = 0
    process_num = 0
    tool_name= ''
    run_name = argvs[0]
    argv = argvs[1:]
    usage_tip = 'usage: '+run_name+' -s <start_index> -n <total> -t <tool_name> -p <process_num>'
    try:
        opts, args = getopt.getopt(argv,"hs:n:t:p:",["help","start_index=","total=","tool_name=","process_num="])
    except getopt.GetoptError:
        print 'GetoptError,' + usage_tip
        print "+------------------------------------+"
        print "| detect tools selection:1/2/3/4/5/6 |"
        print "| tool-1 =>  sanliuling              |"
        print "| tool-2 =>  jinshan                 |"
        print "| tool-3 =>  tencentmanager          |"
        print "| tool-4 =>  baidudefender           |"
        print "| tool-5 =>  macfree                 |"
        print "| tool-6 =>  virustotal              |"
        print "+------------------------------------+"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print "+------------------------------------+"
            print "| detect tools selection:1/2/3/4/5/6 |"
            print "| tool-1 =>  sanliuling              |"
            print "| tool-2 =>  jinshan                 |"
            print "| tool-3 =>  tencentmanager          |"
            print "| tool-4 =>  baidudefender           |"
            print "| tool-5 =>  macfree                 |"
            print "| tool-6 =>  virustotal              |"
            print "+------------------------------------+"
            print usage_tip
            sys.exit()
        elif opt in ("-s", "--start_index"):
            start_index = arg
        elif opt in ("-n", "--total"):
            total = arg
        elif opt in ("-t","--tool_name"):
            tool_name = arg
        elif opt in ("-p", "--process_num"):
            process_num = arg

    return start_index,total,tool_name,process_num

if __name__=="__main__":
    print command_parse(sys.argv)