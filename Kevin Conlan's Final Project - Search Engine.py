#Kevin's final project - search engine   
#Python - Gula Nurmatova

import urllib


max_limit= 510
def get_webpage(url):     #This function will return webpage contents
    try:
        f = urllib.urlopen(url)
        page = f.read()
        f.close()
        return page
    except:	
        return ""
    return ""
def list_merge(a,b):#This function will merge the second list into first, without duplicating an element of a if it's already in a
        if e not in a:
            a.append(e)

def get_next_url(page):
    first_link=page.find("a href")
    if(first_link==-1):
        return None,0
    first_quote=page.find('"',first_link)
    end_quote=page.find('"',first_quote+1)
    url=page[start_quote+1:end_quote]
    return url,end_quote

def get_links(page):
    links=[]
    while(True):
        url,n=get_next_url(page)
        page=page[n:]
        if url:
            links.append(url)
        else:
            break
    return links

def find_links(index,keyword): #This function finds the keywords in the index and returns the list of links
    #f=[]
    if keyword in index:
        return index[keyword]
    return []
#The format of items in the index will be <keyword>,[<List of urls with keyword>]

def add_to_index(index,url,keyword):
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append(url)
        return
    index[keyword]=[url]
    
def add_page_to_index(index,url,content): #Adds the content of a webpage index
    for i in content.split():
        add_to_index(index,url,i)

def get_ranks(graph):#Computing ranks for all the links in a given graph
    d=0.8
    loops=10
    ranks={}
    pages=len(graph)
    for page in graph:
        ranks[page]=1.0/pages
    for i in range(0,loops):
        newranks={}
        for page in graph:
            newrank=(1-d)/pages
            for node in graph:
                if page in graph[node]:
                    newrank=newrank+d*ranks[node]/len(graph[node])
            newranks[page]=newrank
        ranks=newranks
    return ranks

def web_crawler(seed):#The website that will be the seed is given as input
    tocrawl=[seed]
    crawled=[]
    index={}
    graph={}
    global max_limit
    while tocrawl:
        p=tocrawl.pop()
        if p not in crawled:# if a page is already crawled, it won't be crawled again
            max_limit-=1
            print max_limit
            if max_limit<=0:
                break
            c=get_page(p)
            add_page_to_index(index,p,c)
            f=get_links(c)
            list_merge(tocrawl,f)
            graph[p]=f
            crawled.append(p) #When a link is crawled it is appended to crawled. We will return the crawled since it contains all the links we have 
    return crawled,index,graph #Returns the list of links

#print index	

def quick_sort(pages,ranks):#Sort in descending order
    if len(pages)>1:
        pivot=ranks[pages[0]]
        i=1
        j=1
        for j in range(1,len(pages)):
            if ranks[pages[j]]>pivot:
                pages[i],pages[j]=pages[j],pages[i]
                i+=1
        pages[i-1],pages[0]=pages[0],pages[i-1]
        QuickSort(pages[1:i],ranks)
        QuickSort(pages[i+1:len(pages)],ranks)

def find_new(index,ranks,keyword):
    pages=Look_up(index,keyword)
    print '\nPrinting results \n'
    for i in pages:
        print i+" --> "+str(ranks[i])#Display lists, with page rank along side
    quick_sort(pages,ranks)
    print "\nAfter Sorting by page rank\n"
    it=0
    for i in pages:
        it+=1
        print str(it)+'.\t'+i+'\n' 

print "Enter seed page"
seed_page=raw_input()
print "Enter What you want to search"
search=raw_input()
try:
    print "Enter depth of your search"
    max_limit=int(raw_input())
except:
    f=None
print '\nCrawling, currently at..'
crawled,index,graph=web_crawler(seed_page)#print all links

ranks=get_ranks(graph)#Calculate the page ranks
Look_up_new(index,ranks,search_term)