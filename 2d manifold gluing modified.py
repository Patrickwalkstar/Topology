def generate_polygon_verteces():
    gluing=input("please input gluing here:")
    edges=gluing.split(',')
    check_edges=[]
    a=0
    while a < len(edges) :
        edge=edges[a]
        if edge[0] == '-' : #edge is counterclockwise
            edge_placeholder=edge[1:] #check_Edges is just a list of edge identities present, we don't care about direction
        else:
            edge_placeholder=edge[:] #no data will be present other than identity, no '-' assumes clockwise
        if edge_placeholder in check_edges:
            edge=edge+'2' #if we already have the identity in check edges, we don't need to collect the identity again, but we want to
            #marke the edge as the second one of its identity (this is just to make later code possible)
        else:
            check_edges.append(edge_placeholder) #if the edge has a new identity, we want to record it in check_edges for later consideration
        edges[a]=edge
        a=a+1
    relationships={} #this dictionary is going to be a relationship of arbitrary points on each edge. there are going to be two points
    #assigned for each edge, one upper and lower. These 'points' will get used for determining which vertexes on the polygon are actually
    #the same vertex in the glued manifolds polygonilization.
    #so each edge needs one point corresponding to each vertex that edge connects to.
    a=0
    while a < len(edges) :
        edge=edges[a] #the edge being considered

        if edge[0] == '-': # if the considered edge being considered is counterclockwise

            if a == 0: # if the edge is the first in the edge list
                upper=len(edges)-1 # the upper connection will be the next edge counterclockwise, which is actually the last edge
                #listed in the edges list
                lower=a+1 # the lower connection will be the next edge clockwise, which is the next edge in the edge list
            
            elif a == len(edges)-1 : # if the edge being considered is the last edge in the list
                upper=a-1 # the upper connection will be the next edge counterclockwise, which is the previous edge in the edge list
                lower=0 # the lower connection will be the next edge clockwise, which is actually the first edge in the edge list
            
            else: # if the edge being considered is not the last edge or first edge
                upper = a-1 #the upper connection will be the next edge counterclockwise, which is the next edge in the edge list
                lower = a+1 #the lower connection will be the next edge clockwise, which is the previous edge in the edge list
            
            edge_lower=edges[lower] #this actually pulls the edge from index we found earlier, lower represents index of the lower connection
            #edge_lower represents edge connecting to the lower connection of our considered edge
        
            if edge_lower[0] == '-': #if the lower connection edge is counterclocwise
                edge_lower=edge_lower+' upper' #then the lower connection of our considered edge actually connects to the upper connection
                #of the lower connecting edge
            
            else:   #the lower connection edge is clockwise
                edge_lower=edge_lower+' lower' #then the lower connection of our considered edge actually connects to the lower connection
                # of the lower connecting edge

            edge_upper=edges[upper] # this actually pulls the edge from index we found earlier, upper represents index of the lower connection
            #edge_upper represents edge connecting to the upper connection of our considered edge

            if edge_upper[0] == '-': #if the lower connection edge is counterclockwise
                edge_upper=edge_upper+' lower' #the upper connection of our considered edge actually connects to the lower connection
                #of the upper connecting edge
            
            else: #if the lower connection edge is clockwise
                edge_upper=edge_upper+' upper' #the upper connection of our considered eddge actually connects to the upper connection
                #of the upper connecting edge

        else: #if the considered edge is clocwise orientation
            if a == 0 : # if the considered edge is the first in the edge list
                upper = a+1 # the upper connection will be the next edge clockwise, which is the next edge in the edge list
                lower = len(edges)-1 # the lower connection will be the next edge counterclockwise, which is the last edge in the edge list
            
            elif a == len(edges)-1 :# if the considered edge is the last edge in the edge list
                upper = 0 # the upper connection will be the next edge clockwise, which is the first edge in the edge list
                lower = a-1 # the lower connection will be the next edge counterclockwise, which is the previous edge in the edge list

            else: # if the edge considered is not the first or last in the edge list
                upper = a+1 # the upper connection will be the next edge clockwise, which is the next edge in the edge list
                lower= a-1 # the lower connection will be the next edge counterclockwise, which is the previous edge in the edge list

            edge_lower=edges[lower]
            if edge_lower[0] == '-': #if the connecting edge is counterclocwise
                edge_lower=edge_lower+' lower' #the lower connection of the considered edgeactuallly connects to the lower connection
                #of the lower connecting edge

            else: # if the connecting edge is clockwise
                edge_lower=edge_lower+' upper' # the lower connection of the consdiered edge actually connects to the upper connection
                #of the lower connecting edge

            edge_upper=edges[upper]
            if edge_upper[0] == '-': #if the upper connecting edge is clockwise
                edge_upper=edge_upper+' upper' #the upper connection of the considered edge actually connects to the upper connection
                #of the upper connecting edge

            else: #if the upper connecting edge is counterclockwise
                edge_upper=edge_upper+' lower' #the upper connection of the considered edge actually connects to the lower connection
                #of the upper connecting edge

        relationships[str(edge)+' upper']=edge_upper# this line establishes the relationship of the upper connection of the considered edge
        #and adds it to our relationships dictionary for later use

        relationships[str(edge)+' lower']=edge_lower# this line establishes the relationship of the lower connection of the considered edge
        #and adds it to our relationships dictionary for later use

        a=a+1 # and then we consider the next edge.

    return relationships,check_edges,edges #relationships,check_edges,edges are the three values we need to know

relationships,check_edges,edges=generate_polygon_verteces()

def determine_boundary_edges(check_edges,edges) :
    boundaries=[] #this list is going to hold all of the edge identities that represent boundary edges

    for item in check_edges: #pick an item in our list of edge identities (check_edges)
        if item[0] == '-':
            item=item[1:]
        if '-'+item+'2' not in edges and item+'2' not in edges: #for a side A, there are two possible notations for the second edge based
            #on how we modified it earlier, -A2 or A2. so we check if either of these appear in the edge list.

            boundaries.append(item) #if neither do, that means that edge identity only has one edge on the polygon, and thus does not glue
            #to any other edge, thus it must be a boundary edge.

    return boundaries #we then return boundaries for later use

boundaries=determine_boundary_edges(check_edges,edges)

def determine_verteces(relationships,boundaries):
    # for this function, we have two arbitrary points for each line, a 'lower' connection and 'upper' connection which represent the
    #verteces of the polygon. we also have all of these points found as keys in our relationships dictionary, so we can quickly grab
    #them all by just using the .keys() function already present in python to grab the keys, and convert them to a list for ease
    #of use later
    edges_split=list(relationships.keys()) 
    verteces=[] #this list is going to be built on later, by adding the connection 'points' that we defined early that relate to the
    #same vertex in the glued polygon as their own sublists. thus the number of vertexes will just be a list, and you can also modify
    #the code to see what edges connect to what verteces, possibly enabling the use of this code in building a visualizer for the actual
    #2D manifold
    boundaries2=[]# this list is going to hold all of the boundary edge connection 'points', which are defined in the next loop
    a=0
    while a < len(boundaries) :
        upper=boundaries[a]+' upper' #create an upper connection string
        lower=boundaries[a]+' lower' #create a lower connection string
        boundaries2.append(upper) #append the upper connection string
        boundaries2.append(lower) #append the lower connection string
        a=a+1
    #at this point, the boundaries 2 list is of the same format as the edges_split, but only containing those related to the boundaries.
    #for ease of coding, we first start at boundary conditions for circle tracing around polygon verteces, as these area segments that
    #start at boundaries have to end at other boundaries, and you can't return to a point you already passed through (because the boundary
    #edges don't glue to other edges, a point on that edge only has one way to approach it from inside the polygon, you can't attack the
    #other side by passing through the edges glued opposite)
    #if we don't start at boundary conditions, then you may accidently define a vertex only partially, leading to doubling of the vertex
    #in the verteces list, or worse
    b=0#arbitrarily, we are going to grab the first boundary edge connection in the boundaries2 list and start form there
    while b < len(boundaries2) : #as long as there are unused points in the boundaries2 list, the following code will be repeated
        startpoint=boundaries2[b]#this is where we will start our ray tracing for this vertex
        boundaries2.remove(startpoint)#we remove the 'point' from boundaries2 to represent that we have now passed a ray through it, so we
        #no longer need to know it exists
        Next2=startpoint#this just changes some terminology to make it fit the loop below
        complete=False#this sets the condition for when to continue the loop below, and when to stop, complete = True when we reach the
        #starting point again, or reach a boundary edge, though we now we can't reach our startpoint again, so we are only concerned with
        #the second condition
        list_holder=[]#this is a fresh and empty list to hold the 'points' that are related to the vertex we will now begin defining in the loop
        while complete==False:#until the loop is complete we keep doing the next steps
            list_holder.append(Next2)#we append Next2, because its a point we have reached in defining this vertex, so it is related to that vertex
            edges_split.remove(Next2)#we also remove Next2 from edges_split to notate that we have used this point already
            Next1=relationships[Next2]#Next1 is the related point that we defined in our relationships dictionary. If you follow the rules
            #of the circle tracing, you'll go this point next
            if Next1 in boundaries2: #if this happens to be a boundary, that means we finished our loop
                boundaries2.remove(Next1) #remove it from the boundaries list
                edges_split.remove(Next1) #remove if from the edges list
                complete=True #and set the complete to true to end the loop
            else: #its not a boundary, so we have to continue the loop
                #now that our circle tracing has led us to an edge that is not a boundary, we want to skip over to the glued edge to continue
                #all of the 'placeholder' variable code deals with that, determines identity, and saves lower vs. upper, so that we can skip
                #to the right point on the glued edge.
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
                Next2=Next2+' '+placeholder2 #Next2 is the point that we skip to via gluing, but we don't know yet if the glued edge is
                #clockwise or counterclowise
                if Next2 not in edges_split: #so Next2 represents the potential clockwise opposite gluing, if that doesn't exist, the
                    #glued edge is the counterclockwise orientation, so we save that.
                    Next2='-'+Next2
                edges_split.remove(Next1)
            list_holder.append(Next1)
            #we add Next1 to our list_holder, a temporary list organizer for collecting points related to one vertex
            #then we repeate the loop if we reached this point
        verteces.append(list_holder) #once a loop has ended, we append all the points we have saved as a single item to the Verteces list,
        #and then return to line 148.

    #at this point, no more boundary conditions remain as possible options to use in the edges list, so we can now start picking arbitrary
    #points and begin circle tracing until we return to our starting point, with no fear of running into a boundary condition, there are no
    #more present. the following code is extremely similar to the previous loop structure for dealing with the verteces attached to boundary
    #edges
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
                edges_split.remove(Next2)
            if Next2 == startpoint:
                complete=True
            
        verteces.append(list_holder)

    return verteces,edges_split

verteces,edges_split=determine_verteces(relationships,boundaries)

def determine_number_of_edges(edges,boundaries):
    number_of_edges=((len(edges)-len(boundaries))/2)+len(boundaries) #this line calculates the number of codes, all edges that aren't boudnaries
    #are actually the same edge as the edge it glues to, so the total number of edges is equal to the number of edges that have gluing partners,
    #dividied by 2. this number is found by subtracting the number of boundaries from the number of edges, and dividing by 2. But, the boundaries
    #are also edges, so we have to add them back in
    return number_of_edges# we return this number for use in calculating the euler characteristic

number_of_edges=determine_number_of_edges(edges,boundaries)

def euler_characteristic(verteces,number_of_edges) :
    Euler=len(verteces)-number_of_edges+1#the Euler characteristic is the number of verteces, minus the number of edges, plus the number of faces
    #we already calculated the number of edges, and because we have a single polygon, we have one face. thus, we also use the len of the verteces
    #list we calculated earlier to get the number of verteces. Thus, the Euler characteristic is determined
    return Euler #we return this for use in calculating the genus of the surface

Euler=euler_characteristic(verteces,number_of_edges)

def determine_orientability(edges,check_edges,boundaries):
    orientable=True # we assume orientability is true, until we find a condition which makes the surface not orientable
    e=0
    while e < len(check_edges):#we have to check each edge pairing in the system to determine if a mobius strip exists
        if orientable == True:#if we have yet to find a mobius strip, we keep looking for one
            check1=check_edges[e]
            if check1 not in boundaries:#if the edge is a boundary, we don't care about if for determining orientability
                if check1 in edges:#the first occurence of the edge identity has a clockwise orientation
                    check2=check1+'2'
                    if check2 in edges:#if the second occurence of the edge identity also has a clockwise orientation, then the orientability is false
                        orientable = False #set orientable to false
                        e=e+len(check_edges)
                else: #the first occurence of the edge identity has a counterclockwise orientation
                    check2='-'+check1+'2'
                    if check2 in edges:# if the second occurence of the edge identity also has a counterclockwise orientation, then the orientability is false
                        orientable = False #set orientable to false
                        e=e+len(check_edges)
            e=e+1 #move on to check the next edge
    return orientable #return orientability to display, and also use in calculating genus

orientable=determine_orientability(edges,check_edges,boundaries)

def determine_compacted_boundaries(edges, boundaries):
    compacted_boundaries=len(boundaries)
    for item in boundaries:
        print('compacted_boundaries')
        print(compacted_boundaries)
        index=edges.index(item)
        print(index)
        if index == 0:
            if edges[-1] in boundaries:
                compacted_boundaries=compacted_boundaries-.5
            if edges[1] in boundaries:
                compacted_boundaries=compacted_boundaries-.5
        elif index == len(edges)-1:
            if edges[0] in boundaries:
                compacted_boundaries=compacted_boundaries-.5
            if edges[-2] in boundaries:
                compacted_boundaries=compacted_boundaries-.5
        else:
            if edges[index-1] in boundaries:
                compacted_boundaries = compacted_boundaries-.5
            if edges[index+1] in boundaries:
                compacted_boundaries = compacted_boundaries-.5
    if len(boundaries) != 0 and compacted_boundaries == 0:
        compacted_boundaries = 1
    return compacted_boundaries

compacted_boundaries = determine_compacted_boundaries(edges,boundaries)

def determine_genus(Euler,orientable,compacted_boundaries):
    if orientable == True:
        genus=0-((Euler+compacted_boundaries-2)/2) # if the surface is orientable, this equation allows you to calculate the genus
    else:
        genus=0-(Euler+compacted_boundaries-2) #if the surface is not orientable, this equation allows you to calculate the genus
    return(genus)

genus=determine_genus(Euler,orientable,compacted_boundaries)

print('the Euler characteristic is ' +str(Euler))
print('there are ' +str(compacted_boundaries) +' boundaries')
if orientable == False:
    print('the surface is not orientable')
else:
    print('the surface is orientable')
print ('the genus of the surface is ' +str(genus))