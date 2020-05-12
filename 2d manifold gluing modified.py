def generate_polygon_verteces():
    gluing=input("please input gluing here:")
    edges=gluing.split(',')
    check_edges=[]
    a=0
    while a < len(edges) :
        edge=edges[a]
        if edge[0] == '-' :
            edge_placeholder=edge[1:]
        else:
            edge_placeholder=edge[:]
        if edge_placeholder in check_edges:
            edge=edge+'2'
        else:
            check_edges.append(edge)
        edges[a]=edge
        a=a+1
    relationships={}
    a=0
    while a < len(edges) :
        edge=edges[a]
        if edge[0] == '-':
            if a == 0:
                upper=len(edges)-1
                lower=a+1
            elif a == len(edges)-1 :
                upper=a-1
                lower=0
            else:
                upper = a-1
                lower = a+1
            edge_lower=edges[lower]
            if edge_lower[0] == '-':
                edge_lower=edge_lower+' upper'
            else:
                edge_lower=edge_lower+' lower'
            edge_upper=edges[upper]
            if edge_upper[0] == '-':
                edge_upper=edge_upper+' lower'
            else:
                edge_upper=edge_upper+' upper'
        else:
            if a == 0 :
                upper = a+1
                lower = len(edges)-1
            elif a == len(edges)-1 :
                upper = 0
                lower = a-1
            else:
                upper = a+1
                lower= a-1
            edge_lower=edges[lower]
            if edge_lower[0] == '-':
                edge_lower=edge_lower+' lower'
            else:
                edge_lower=edge_lower+' upper'
            edge_upper=edges[upper]
            if edge_upper[0] == '-':
                edge_upper=edge_upper+' upper'
            else:
                edge_upper=edge_upper+' lower'
        relationships[str(edge)+' upper']=edge_upper
        relationships[str(edge)+' lower']=edge_lower
        a=a+1
    return relationships,check_edges,edges

relationships,check_edges,edges=generate_polygon_verteces()

def determine_boundary_edges(check_edges,edges) :
    boundaries=[]
    for item in check_edges:
        if '-'+item+'2' not in edges and item+'2' not in edges:
            boundaries.append(item)
    return(boundaries)

boundaries=determine_boundary_edges(check_edges,edges)

def determine_verteces(relationships,check_edges,boundaries):
    edges_split=list(relationships.keys())
    print(edges_split)
    verteces=[]
    boundaries2=[]
    a=0
    while a < len(boundaries) :
        upper=boundaries[a]+' upper'
        lower=boundaries[a]+' lower'
        boundaries2.append(upper)
        boundaries2.append(lower)
        a=a+1
    b=0
    while b < len(boundaries2) :
        startpoint=boundaries2[b]
        boundaries2.remove(startpoint)
        complete=False
        list_holder=[]
        while complete==False:
            list_holder.append(startpoint)
            edges_split.remove(startpoint)
            Next1=relationships[startpoint]
            if Next1 in boundaries2:
                boundaries2.remove(Next1)
                edges_split.remove(Next1)
                complete=True
            else:
                placeholder=Next1[:]
                if placeholder[0]=='-':
                    placeholder=placeholder[1:]
                placeholder=placeholder.split(' ')
                placeholder1=placeholder[0]
                placeholder2=placeholder[1]
                if placeholder1[-1]=='2':
                    Next2=placeholder1[0:len(placeholder1)-1]
                else:
                    Next2=placeholder1+'2'
                Next2=Next2+' '+placeholder2
                edges_split.remove(Next1)
                if Next2 in edges_split:
                    startpoint=Next2
                else:
                    startpoint='-'+Next2
            list_holder.append(Next1)
        verteces.append(list_holder)
    b=0
    while b < len(edges_split):
        startpoint=edges_split[b]
        Next2=startpoint[:]
        complete=False
        list_holder=[]
        while complete == False:
            list_holder.append(Next2)
            Next1=relationships[Next2]
            edges_split.remove(Next1)
            list_holder.append(Next1)
            placeholder=Next1.split(' ')
            placeholder1=placeholder[0]
            placeholder2=placeholder[1]
            if placeholder1[0]=='-':
                placeholder=placeholder1[1:]
            else:
                placeholder=placeholder1[:]
            if placeholder[-1]=='2':
                placeholder=placeholder[0:(len(placeholder)-1)]
            else:
                placeholder=placeholder+'2'
            placeholder=placeholder+' '+placeholder2
            if placeholder in edges_split:
                Next2=placeholder
                edges_split.remove(Next2)
            else:
                Next2='-'+placeholder
                print(Next2)
                print(edges_split)
                edges_split.remove(Next2)
            if Next2 == startpoint:
                complete=True
            
        verteces.append(list_holder)

    return verteces,edges_split

verteces,edges_split=determine_verteces(relationships,check_edges,boundaries)

def determine_number_of_edges(edges,boundaries):
    number_of_edges=((len(edges)-len(boundaries))/2)+len(boundaries)
    return(number_of_edges)

number_of_edges=determine_number_of_edges(edges,boundaries)

def euler_characteristic(verteces,number_of_edges) :
    Euler=len(verteces)-number_of_edges+1
    return Euler

Euler=euler_characteristic(verteces,number_of_edges)

def determine_orientability(edges,check_edges,boundaries):
    orientable=True
    e=0
    while e < len(check_edges):
        if orientable == True:
            check1=check_edges[e]
            if check1 not in boundaries:
                if check1 in edges:
                    check2='-'+check1+'2'
                    if check2 not in edges:
                        orientable = False
                        e=e+len(check_edges)
                else:
                    check2=check1+'2'
                    if check2 not in edges:
                        orientable = False
                        e=e+len(check_edges)
            e=e+1
    return orientable

orientable=determine_orientability(edges,check_edges,boundaries)

def determine_genus(Euler,orientable,boundaries):
    if orientable == True:
        genus=0-((Euler+len(boundaries)-2)/2)
    else:
        genus=0-(Euler+len(boundaries)-2)
    return(genus)

genus=determine_genus(Euler,orientable,boundaries)

print('the Euler characteristic is ' +str(Euler))
print('there are ' +str(len(boundaries)) +' boundaries')
if orientable == False:
    print('the surface is not orientable')
else:
    print('the surface is orientable')
print ('the genus of the surface is ' +str(genus))