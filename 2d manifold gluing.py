def generate_polygon_verteces():
    gluing=input('please input gluing here (clockwise around polygon, seperate with commas):')
    edges_unmodified=gluing.split(',')
    edges=gluing.split(',')
    checkededges=[]
    i=0
    while i < len(edges):
        if (edges[i])[0] == '-':
            inverse=True
            edges[i]=(edges[i])[1:]
        else:
            inverse=False
        if edges[i] not in checkededges:
            checkededges.append(edges[i])
        else:
            edges[i]=edges[i]+'2'
        if inverse == True:
            edges[i]='-'+edges[i]
        i=i+1
    relationships={}
    i=0
    while i < len(edges):
        side=edges[i]
        if i == len(edges)-1:
            if side[-1] == '2':
                if side[0] == '-':
                    #clockwise
                    upper_relation=edges[0]
                    lower_relation=edges[i-1]
                    if upper_relation[-1] == '2':
                        if upper_relation[0] == '-':
                            #clockwise
                            upper_relation=upper_relation + ' lower'
                        else:
                            #counterclockwise
                            upper_relation=upper_relation+ ' upper'
                    else:
                        #clockwise
                        upper_relation=upper_relation+ ' lower'
                    if lower_relation[-1] == '2':
                        if lower_relation[0] == '-':
                            #clockwise
                            lower_relation=lower_relation + ' upper'
                        else:
                            #counterclockwise
                            lower_relation=lower_relation+ ' lower'
                    else:
                        #clockwise
                        lower_relation=lower_relation+ ' upper'
                else:
                    #counterclockwise
                    upper_relation=edges[i-1]
                    lower_relation=edges[0]
                    if upper_relation[-1] == '2':
                        if upper_relation[0] == '-':
                            #clockwise
                            upper_relation=upper_relation + ' upper'
                        else:
                            #counterclockwise
                            upper_relation=upper_relation+ ' lower'
                    else:
                        #clockwise
                        upper_relation=upper_relation+ ' upper'
                    if lower_relation[-1] == '2':
                        if lower_relation[0] == '-':
                            #clockwise
                            lower_relation=lower_relation + ' lower'
                        else:
                            #counterclockwise
                            lower_relation=lower_relation+ ' upper'
                    else:
                        #clockwise
                        lower_relation=lower_relation+ ' lower'
            else:
                #clockwise
                upper_relation=edges[0]
                lower_relation=edges[i-1]
                if upper_relation[-1] == '2':
                    if upper_relation[0] == '-':
                        #clockwise
                        upper_relation=upper_relation + ' lower'
                    else:
                        #counterclockwise
                        upper_relation=upper_relation+ ' upper'
                else:
                    #clockwise
                    upper_relation=upper_relation+ ' lower'
                if lower_relation[-1] == '2':
                    if lower_relation[0] == '-':
                        #clockwise
                        lower_relation=lower_relation + ' upper'
                    else:
                        #counterclockwise
                        lower_relation=lower_relation+ ' lower'
                else:
                    #clockwise
                    lower_relation=lower_relation+ ' upper'
        else:
            if side[-1] == '2':
                if side[0] == '-':
                    #clockwise
                    upper_relation=edges[i+1]
                    lower_relation=edges[i-1]
                    if upper_relation[-1] == '2':
                        if upper_relation[0] == '-':
                            #clockwise
                            upper_relation=upper_relation + ' lower'
                        else:
                            #counterclockwise
                            upper_relation=upper_relation+ ' upper'
                    else:
                        #clockwise
                        upper_relation=upper_relation+ ' lower'
                    if lower_relation[-1] == '2':
                        if lower_relation[0] == '-':
                            #clockwise
                            lower_relation=lower_relation + ' upper'
                        else:
                            #counterclockwise
                            lower_relation=lower_relation+ ' lower'
                    else:
                        #clockwise
                        lower_relation=lower_relation+ ' upper'
                else:
                    #counterclockwise
                    upper_relation=edges[i-1]
                    lower_relation=edges[i+1]
                    if upper_relation[-1] == '2':
                        if upper_relation[0] == '-':
                            #clockwise
                            upper_relation=upper_relation + ' upper'
                        else:
                            #counterclockwise
                            upper_relation=upper_relation+ ' lower'
                    else:
                        #clockwise
                        upper_relation=upper_relation+ ' upper'
                    if lower_relation[-1] == '2':
                        if lower_relation[0] == '-':
                            #clockwise
                            lower_relation=lower_relation + ' lower'
                        else:
                            #counterclockwise
                            lower_relation=lower_relation+ ' upper'
                    else:
                        #clockwise
                        lower_relation=lower_relation+ ' lower'
            else:
                #clockwise
                upper_relation=edges[i+1]
                lower_relation=edges[i-1]
                if upper_relation[-1] == '2':
                    if upper_relation[0] == '-':
                        #clockwise
                        upper_relation=upper_relation + ' lower'
                    else:
                        #counterclockwise
                        upper_relation=upper_relation+ ' upper'
                else:
                    #clockwise
                    upper_relation=upper_relation+ ' lower'
                if lower_relation[-1] == '2':
                    if lower_relation[0] == '-':
                        #clockwise
                        lower_relation=lower_relation + ' upper'
                    else:
                        #counterclockwise
                        lower_relation=lower_relation+ ' lower'
                else:
                    #clockwise
                    lower_relation=lower_relation+ ' upper'
        key1=side+' upper'
        key2=side+' lower'
        def1=upper_relation
        def2=lower_relation
        relationships[key1]=def1
        relationships[key2]=def2
        i=i+1
    return (relationships, edges, edges_unmodified)     

def determine_orientability(edges_unmodified):
    orientable=True
    i=0
    while i < len(edges_unmodified) and orientable == True:
        edge=edges_unmodified[i]
        if edge[0]=='-':
            orientable=False
        i=i+1
    return orientable

def determine_boundaries(edges_unmodified):
    boundaries=[]
    edges_holder=[]
    i=0
    while i < len(edges_unmodified):
        edge=edges_unmodified[i]
        if edge[0]=='-':
            edge=edge[1:]
        edges_holder.append(edge)
        i=i+1
    i=0
    print('edges_Holder is ' + str(edges_holder))
    while i < len(edges_holder):
        edge=edges_holder[i]
        other_edges=edges_holder.copy()
        other_edges.remove(edge)
        if edge not in other_edges:
            boundaries.append(edge)
        i=i+1
    return(boundaries)
         

def determine_number_of_verteces(relationships,boundaries,edges):
    verteces=relationships.keys()
    verteces=list(verteces)
    boundaries2=[]
    for item in boundaries:
        upper=item+' upper'
        lower=item+' lower'
        boundaries2.append(upper)
        boundaries2.append(lower)
    i=0
    Actual_verteces=0
    while i < len(boundaries2):
        start=boundaries2[i]
        finished=False
        Next1=start
        boundaries2.remove(Next1)
        verteces.remove(Next1)
        Next2=relationships[Next1]
        while finished==False:
            verteces.remove(Next2)
            if Next2 in boundaries2:
                finished=True
                boundaries2.remove(Next2)
                Actual_verteces=Actual_verteces+1
            else:
                placeholder=Next2.split(' ')
                edge=placeholder[0]
                orientation=placeholder[1]
                if edge[-1]=='2':
                    if edge[0]=='-':
                        Next3=edge[1:len(edge)-1]
                    else:
                        Next3=edge[0:len(edge)-1]
                else:
                    check='-'+edge+'2'
                    if check in edges:
                        Next3=check
                    else:
                        Next3=edge+'2'
                Next4=Next3+' '+orientation
                verteces.remove(Next4)
                Next1=Next4
                Next2=relationships[Next1]
    i=0
    while i < len(verteces):
        start=verteces[i]
        finished=False
        Next1=start
        verteces.remove(Next1)
        while finished == False:
            Next2=relationships[Next1]
            verteces.remove(Next2)
            placeholder=Next2.split(' ')
            edge=placeholder[0]
            orientation=placeholder[1]
            if edge[-1]=='2':
                if edge[0]=='-':
                    Next3=edge[1:len(edge)-1]
                else:
                    Next3=edge[0:len(edge)-1]
            else:
                check='-'+edge+'2'
                if check in edges:
                    Next3=check
                else:
                    Next3=edge+'2'
            Next4=Next3+' '+orientation
            if Next4 == start:
                finished=True
                Actual_verteces=Actual_verteces+1
            else:
                verteces.remove(Next4)
                Next1=Next4
    return (Actual_verteces)



def calculate_euler_number(Actual_verteces,edges_unmodified,boundaries):
    triangulation_edges=((len(edges_unmodified)-len(boundaries))/2)+len(boundaries)
    x=Actual_verteces-triangulation_edges+1
    return x

def calculate_genus(x,boundaries,orientable):
    if orientable ==True:
        genus=(2-x-len(boundaries))/2
    else:
        genus=2-x-len(boundaries)
    return genus

relationships,edges,edges_unmodified=generate_polygon_verteces()
boundaries=determine_boundaries(edges_unmodified)
orientable=determine_orientability(edges_unmodified)
Actual_verteces=determine_number_of_verteces(relationships,boundaries,edges)
x=calculate_euler_number(Actual_verteces,edges_unmodified,boundaries)
genus=calculate_genus(x,boundaries,orientable)
print('the number of boundaries is ' + str(len(boundaries)))
print('euler characteristic is ' + str(x))
print('the surface is orientable? ' +str(orientable))
print('genus is ' + str(genus))