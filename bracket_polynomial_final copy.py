import copy

def collect_parametrized_knot():
    information=open("knot parametrization input.txt","r")
    information=information.readlines()
    information=information[8:]
    information=str(information)
    information=information[2:(len(information)-2)]
    information=information.split()
    for i in range(len(information)):
        strand_considered=information[i]
        if i==0:
            strand_considered=strand_considered[0:len(strand_considered)-4]
        elif i==(len(information)-1):
            strand_considered=strand_considered[1:len(strand_considered)]
        else:
            strand_considered=strand_considered[1:len(strand_considered)-4]
        information[i]=strand_considered
    parametrization=list()
    for i in range(len(information)):
        strand_considered=information[i]
        List=strand_considered.split(',')
        for i in range(len(List)):
            item_considered=List[i]
            if i%2==0:
                item_considered=item_considered[1:]
            else:
                item_considered=item_considered[0:(len(item_considered)-1)]
            List[i]=item_considered
        new_List=list()
        for i in range(0,len(List),2):
            List[i+1]=int(float(List[i+1]))
            new_item=list([List[i],List[i+1]])
            new_List.append(new_item)
        List=new_List
        parametrization.append(List)
    return (parametrization)

def check_intersections(knot_unperturbed):
    intersections=list()
    a=0
    while a < len(knot_unperturbed):
        strand_considered=knot_unperturbed[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0] not in intersections:
                intersections.append(intersection_considered[0])
            b=b+1
        a=a+1
    return intersections

def reverse_strands(knot_unperturbed,initial_strand,intersection):
    knot2=copy.copy(knot_unperturbed)
    strands_to_flip=list()
    strands_to_flip.append(initial_strand)
    intersection_check=initial_strand[-1]
    a=0
    while a < len(knot2) and intersection_check[0] != intersection:
        strand_considered=knot2[a]
        intersection_considered=strand_considered[0]
        if intersection_considered[0]==intersection_check[0] and intersection_considered[1]==-(intersection_check[1]):
            strands_to_flip.append(strand_considered)
            intersection_check=strand_considered[-1]
            a=0
        else:
            a=a+1
    strands_flipped=list()
    a=0
    while a < len(strands_to_flip):
        strand_considered=strands_to_flip[a]
        knot2.remove(strand_considered)
        b=1
        strand_flipped=list()
        while b<(len(strand_considered)+1):
            strand_flipped.append(strand_considered[-b])
            b=b+1
        strands_flipped.append(strand_flipped)
        knot2.append(strand_flipped)
        a=a+1
    intersections_flipped=list()
    a=0
    while a < len(strands_flipped):
        strand_considered=strands_flipped[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[1]==0 and intersection_considered[0] != intersection:
                intersections_flipped.append(intersection_considered[0])
            b=b+1
        a=a+1
    a=0
    while a < len(knot2):
        strand_considered=knot2[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0] in intersections_flipped:
                if intersection_considered[1]==1:
                    intersection_considered[1]=-1
                elif intersection_considered[1]==-1:
                    intersection_considered[1]=1
            b=b+1
        a=a+1
    #a=0
    #print(strands_flipped)
    #while a < len(strands_flipped):
    #    strand_considered=strands_flipped[a]
    #    b=0
    #    while b < len(strand_considered):
    #        intersection_considered=strand_considered[b]
    #        if intersection_considered[0] in intersections_flipped:
    #            if intersection_considered[1]==1:
    #                intersection_considered[1]=-1
    #            elif intersection_considered[1]==-1:
    #                intersection_considered[1]=1
    #        b=b+1
    #    a=a+1
    return knot2, strands_flipped

def split_intersection_A(knot_unperturbed,intersection):
    knot=0
    knot=copy.deepcopy(knot_unperturbed)
    a=0
    while a < len(knot):
        strand_considered=knot[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0]==intersection and intersection_considered[1]==0:
                intersection_considered_2=strand_considered[0]
                if intersection_considered_2[1]==1 or intersection_considered_2[1]==-1:
                    strandsplit1=strand_considered[0:b+1]
                    strandsplit2=strand_considered[b:]
                elif intersection_considered_2[1]==0:
                    if b!=0:
                        strandsplit1=strand_considered[-b:b+1]
                        strandsplit2=strandsplit1[:]
                    elif b==0:
                        strandsplit1=copy.copy(strand_considered)
                        strandsplit1.append(strand_considered[0])
                        strandsplit2=strandsplit1[:]
                remove=strand_considered
            b=b+1
        a=a+1
    knot.remove(remove)
    knot.append(strandsplit1)
    knot.append(strandsplit2)
    a=0
    while a < len(knot):
        strand_considered=knot[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0]==intersection and intersection_considered[1]==1:
                strand_positive=strand_considered[:]
                if b==0:
                    positive_orientation=True
                else:
                    positive_orientation=False
            if intersection_considered[0]==intersection and intersection_considered[1]==-1:
                strand_negative=strand_considered[:]
            b=b+1
        a=a+1
    if positive_orientation==True:
        if strand_positive == strandsplit1 and strand_negative != strandsplit2:
            strandnew1=list()
            strandnew2=list()
            strandnew1=strand_positive[1:(len(strand_positive)-1)]
            a=0
            while a <(len(strand_negative)-1):
                strandnew2.append(strand_negative[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)):
                strandnew2.append(strandsplit2[a])
                a=a+1
            knot.remove(strand_positive)
            knot.remove(strandsplit2)
            knot.remove(strand_negative)
            knot.append(strandnew1)
            knot.append(strandnew2)
        elif strand_positive ==strandsplit1 and strand_negative == strandsplit2:
            strandnew1=list()
            strandnew2=list()
            strandnew1=strand_positive[1:(len(strand_positive)-1)]
            strandnew2=strand_negative[1:(len(strand_negative)-1)]
            knot.remove(strand_positive)
            knot.remove(strand_negative)
            knot.append(strandnew1)
            knot.append(strandnew2)
        elif strand_positive != strandsplit1 and strand_negative == strandsplit2:
            strandnew1=list()
            strandnew2=list()
            strandnew1=strand_negative[1:(len(strand_negative)-1)]
            a=0
            while a <(len(strandsplit1)-1):
                strandnew2.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strand_positive)):
                strandnew2.append(strand_positive[a])
                a=a+1
            knot.remove(strand_positive)
            knot.remove(strandsplit1)
            knot.remove(strand_negative)
            knot.append(strandnew1)
            knot.append(strandnew2)
        elif strand_positive == strand_negative:
            strandnew1=list()
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot.remove(strand_positive)
            knot.remove(strandsplit1)
            knot.remove(strandsplit2)
            knot.append(strandnew1)
        elif strandsplit1 == strandsplit2:
            strandnew1=list()
            a=0
            while a < (len(strand_negative)-1):
                strandnew1.append(strand_negative[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < (len(strand_positive)):
                strandnew1.append(strand_positive[a])
                a=a+1
            knot.remove(strandsplit2)
            knot.remove(strandsplit1)
            knot.remove(strand_positive)
            knot.remove(strand_negative)
            knot.append(strandnew1)
        else:
            strandnew1=list()
            strandnew2=list()
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < len(strand_positive):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=0
            while a < (len(strand_negative)-1):
                strandnew2.append(strand_negative[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew2.append(strandsplit2[a])
                a=a+1
            knot.remove(strandsplit1)
            knot.remove(strandsplit2)
            knot.remove(strand_positive)
            knot.remove(strand_negative)
            knot.append(strandnew1)
            knot.append(strandnew2)
    elif positive_orientation==False:
        if strandsplit1==strand_negative and strandsplit2==strand_positive:
            strandnew1=list()
            knot,strands_flipped=reverse_strands(knot, strandsplit2, intersection)
            strandsplit2=strands_flipped[0]
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            knot.remove(strandsplit2)
            knot.remove(strandsplit1)
            knot.append(strandnew1)
        elif strandsplit1 == strand_negative and strandsplit2 != strand_positive:
            strandnew1=list()
            knot,strands_flipped=reverse_strands(knot,strandsplit1,intersection)
            strandsplit1=strands_flipped[0]
            a=0
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot.remove(strandsplit1)
            knot.remove(strandsplit2)
            knot.remove(strand_positive)
            knot.append(strandnew1)
        elif strandsplit1 != strand_negative and strandsplit2 == strand_positive:
            strandnew1=list()
            knot,strands_flipped=reverse_strands(knot,strandsplit2,intersection)
            strandsplit2=strands_flipped[0]
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < len(strand_negative):
                strandnew1.append(strand_negative[a])
                a=a+1
            knot.remove(strandsplit2)
            knot.remove(strand_negative)
            knot.remove(strandsplit1)
            knot.append(strandnew1)
        elif strandsplit1==strandsplit2:
            strandnew1=list()
            knot,strands_flipped=reverse_strands(knot,strandsplit2,intersection)
            strandsplit2=strands_flipped[0]
            a=0
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < len(strand_negative):
                strandnew1.append(strand_negative[a])
                a=a+1
            knot.remove(strand_negative)
            knot.remove(strandsplit2)
            knot.remove(strandsplit1)
            knot.remove(strand_positive)
            knot.append(strandnew1)
        elif strand_positive==strand_negative:
            strandnew1=list()
            knot,strands_flipped=reverse_strands(knot,strand_negative,intersection)
            strand_negative=strands_flipped[0]
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strand_negative)-1):
                strandnew1.append(strand_negative[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot.remove(strand_negative)
            knot.remove(strandsplit1)
            knot.remove(strandsplit2)
            knot.append(strandnew1)
        else:
            strandnew1=list()
            strandnew2=list()
            knot,strands_flipped=reverse_strands(knot,strandsplit2,intersection)
            strandsplit2=strands_flipped[0]
            strand_considered=strands_flipped[-1]
            intersection_considered=strand_considered[0]
            if intersection_considered[1]==0:
                strandsplit1=strand_considered
                a=0
                while a < (len(strand_positive)-1):
                    strandnew1.append(strand_positive[a])
                    a=a+1
                a=1
                while a < len(strandsplit1):
                    strandnew1.append(strandsplit1[a])
                    a=a+1
                a=0
                while a < (len(strandsplit2)-1):
                    strandnew2.append(strandsplit2[a])
                    a=a+1
                a=1
                while a < len(strand_negative):
                    strandnew2.append(strand_negative[a])
                    a=a+1
            elif intersection_considered[1]==1:
                strand_positive=strand_considered
                a=0
                while a < (len(strandsplit1)-1):
                    strandnew1.append(strandsplit1[a])
                    a=a+1
                a=1
                while a < len(strand_positive):
                    strandnew1.append(strand_positive[a])
                    a=a+1
                a=0
                while a < (len(strandsplit2)-1):
                    strandnew2.append(strandsplit2[a])
                    a=a+1
                a=1
                while a < len(strand_negative):
                    strandnew2.append(strand_negative[a])
                    a=a+1
            knot.remove(strand_negative)
            knot.remove(strand_positive)
            knot.remove(strandsplit1)
            knot.remove(strandsplit2)
            knot.append(strandnew1)
            knot.append(strandnew2)
    return knot

def split_intersection_A_inverse(knot_unperturbed,intersection):
    knot3=copy.deepcopy(knot_unperturbed)
    a=0
    while a < len(knot3):
        strand_considered=knot3[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0]==intersection and intersection_considered[1]==0:
                intersection_considered_2=strand_considered[0]
                if intersection_considered_2[1]==1 or intersection_considered_2[1]==-1:
                    strandsplit1=strand_considered[0:b+1]
                    strandsplit2=strand_considered[b:]
                elif intersection_considered_2[1]==0:
                    if b!=0:
                        strandsplit1=strand_considered[-b:b+1]
                        strandsplit2=strandsplit1[:]
                    elif b==0:
                        strandsplit1=copy.copy(strand_considered)
                        strandsplit1.append(strand_considered[0])
                        strandsplit2=strandsplit1[:]
                remove=strand_considered
            b=b+1
        a=a+1
    knot3.remove(remove)
    knot3.append(strandsplit1)
    knot3.append(strandsplit2)
    a=0
    while a < len(knot3):
        strand_considered=knot3[a]
        b=0
        while b < len(strand_considered):
            intersection_considered=strand_considered[b]
            if intersection_considered[0]==intersection and intersection_considered[1]==1:
                strand_positive=strand_considered[:]
                if b==0:
                    positive_orientation=True
                else:
                    positive_orientation=False
            if intersection_considered[0]==intersection and intersection_considered[1]==-1:
                strand_negative=strand_considered[:]
            b=b+1
        a=a+1
    if positive_orientation==True:
        if strandsplit2 == strand_negative and strandsplit1 == strand_positive:
            strandnew1=list()
            knot3,strands_flipped=reverse_strands(knot3,strand_positive,intersection)
            strand_positive=strands_flipped[0]
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strandsplit2)
            knot3.append(strandnew1)
        elif strandsplit2 == strand_negative and strandsplit1 != strand_positive:
            strandnew1=list()
            knot3,strands_flipped=reverse_strands(knot3,strandsplit2,intersection)
            strandsplit2=strands_flipped[0]
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < len(strand_positive):
                strandnew1.append(strand_positive[a])
                a=a+1
            knot3.remove(strandsplit1)
            knot3.remove(strandsplit2)
            knot3.remove(strand_positive)
            knot3.append(strandnew1)
        elif strandsplit2 != strand_negative and strandsplit1 == strand_positive:
            strandnew1=list()
            knot3,strands_flipped=reverse_strands(knot3,strand_positive,intersection)
            strand_positive=strands_flipped[0]
            a=0
            while a < (len(strand_negative)-1):
                strandnew1.append(strand_negative[a])
                a=a+1
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot3.remove(strandsplit2)
            knot3.remove(strand_negative)
            knot3.remove(strand_positive)
            knot3.append(strandnew1)
        elif strandsplit1 == strandsplit2:
            strandnew1=list()
            knot3,strands_flipped=reverse_strands(knot3,strandsplit2,intersection)
            strandsplit2=strands_flipped[0]
            a=0
            while a < (len(strand_negative)-1):
                strandnew1.append(strand_negative[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < len(strand_positive):
                strandnew1.append(strand_positive[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strandsplit2)
            knot3.remove(strandsplit1)
            knot3.remove(strand_negative)
            knot3.append(strandnew1)
        elif strand_positive==strand_negative:
            strandnew1=list()
            knot3,strands_flipped=reverse_strands(knot3,strand_positive,intersection)
            strand_positive=strands_flipped[0]
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strandsplit1)
            knot3.remove(strandsplit2)
            knot3.append(strandnew1)
        else:
            strandnew1=list()
            strandnew2=list()
            knot3,strands_flipped=reverse_strands(knot3,strand_positive,intersection)
            strand_positive=strands_flipped[0]
            strand_considered=strands_flipped[-1]
            intersection_considered=strand_considered[0]
            if intersection_considered[1]==0:
                strandsplit1=strand_considered
                a=0
                while a < (len(strand_negative)-1):
                    strandnew1.append(strand_negative[a])
                    a=a+1
                a=1
                while a < len(strandsplit1):
                    strandnew1.append(strandsplit1[a])
                    a=a+1
                a=0
                while a < (len(strand_positive)-1):
                    strandnew2.append(strand_positive[a])
                    a=a+1
                a=1
                while a < len(strandsplit2):
                    strandnew2.append(strandsplit2[a])
                    a=a+1
            elif intersection_considered[1]==-1:
                strand_negative=strand_considered
                a=0
                while a < (len(strand_positive)-1):
                    strandnew1.append(strand_positive[a])
                    a=a+1
                a=1
                while a < len(strandsplit2):
                    strandnew1.append(strandsplit2[a])
                    a=a+1
                a=0
                while a < (len(strandsplit1)-1):
                    strandnew2.append(strandsplit1[a])
                    a=a+1
                a=1
                while a < len(strand_negative):
                    strandnew2.append(strand_negative[a])
                    a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strand_negative)
            knot3.remove(strandsplit1)
            knot3.remove(strandsplit2)
            knot3.append(strandnew1)
            knot3.append(strandnew2)
    elif positive_orientation==False:
        if strand_positive == strandsplit2 and strand_negative == strandsplit1:
            strandnew1=list()
            strandnew2=list()
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < (len(strand_negative)-1):
                strandnew2.append(strand_negative[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strand_negative)
            knot3.append(strandnew1)
            knot3.append(strandnew2)
        elif strand_positive == strandsplit2 and strand_negative != strandsplit1:
            strandnew1=list()
            strandnew2=list()
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=0
            while a < (len(strandsplit1)-1):
                strandnew2.append(strandsplit1[a])
                a=a+1
            a=1
            while a < len(strand_negative):
                strandnew2.append(strand_negative[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strandsplit1)
            knot3.remove(strand_negative)
            knot3.append(strandnew1)
            knot3.append(strandnew2)
        elif strand_positive != strandsplit2 and strand_negative == strandsplit1:
            strandnew1=list()
            strandnew2=list()
            a=1
            while a < (len(strand_negative)-1):
                strandnew1.append(strand_negative[a])
                a=a+1
            a=0
            while a < (len(strand_positive)-1):
                strandnew2.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew2.append(strandsplit2[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strandsplit2)
            knot3.remove(strand_negative)
            knot3.append(strandnew1)
            knot3.append(strandnew2)
        elif strandsplit1 == strandsplit2:
            strandnew1=list()
            a=0
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < (len(strandsplit2)-1):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=1
            while a < len(strand_negative):
                strandnew1.append(strand_negative[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strand_negative)
            knot3.remove(strandsplit2)
            knot3.remove(strandsplit1)
            knot3.append(strandnew1)
        elif strand_positive == strand_negative:
            strandnew1=list()
            a=0
            while a < (len(strandsplit1)-1):
                strandnew1.append(strandsplit1[a])
                a=a+1
            a=1
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            knot3.remove(strandsplit1)
            knot3.remove(strandsplit2)
            knot3.remove(strand_positive)
            knot3.append(strandnew1)
        else:
            strandnew1=list()
            strandnew2=list()
            a=0
            while a < (len(strand_positive)-1):
                strandnew1.append(strand_positive[a])
                a=a+1
            a=1
            while a < len(strandsplit2):
                strandnew1.append(strandsplit2[a])
                a=a+1
            a=0
            while a < (len(strandsplit1)-1):
                strandnew2.append(strandsplit1[a])
                a=a+1
            a=1
            while a < len(strand_negative):
                strandnew2.append(strand_negative[a])
                a=a+1
            knot3.remove(strand_positive)
            knot3.remove(strand_negative)
            knot3.remove(strandsplit1)
            knot3.remove(strandsplit2)
            knot3.append(strandnew1)
            knot3.append(strandnew2)
    return knot3

def compile_bracket(bracket):
    compiled_bracket=list()
    for i in range(2,len(bracket),3):
        sign=bracket[i-2]
        exponent=bracket[i-1]
        knot=bracket[i]
        compiled=[sign,exponent,knot]
        compiled_bracket.append(compiled)
    return(compiled_bracket)

def compile_coefficients(bracket):
    polynomial=list()
    a=0
    while a < len(bracket):
        bracket_considered=bracket[a]    
        holder1=bracket_considered[0]
        holder2=bracket_considered[1]
        b=0
        added=False
        while b<len(polynomial) and added==False:
            collected_considered=polynomial[b]
            if holder2 == collected_considered[1]:
                if holder1=='+':
                    collected_considered[0]=collected_considered[0]+1
                elif holder1=='-':
                    collected_considered[0]=collected_considered[0]-1
                added=True
                b=b+1
            else:
                b=b+1
        if b==len(polynomial) and added==False:
            holder1=bracket_considered[0]
            holder2=bracket_considered[1]
            if holder1=='+':
                holder3=1
            elif holder1=='-':
                holder3=-1
            holder4=list([holder3,holder2])
            polynomial.append(holder4)
        a=a+1
    a=0
    n = len(polynomial)
    while a < n:
        exponent_considered=polynomial[a]
        if exponent_considered[0] == 0:
            polynomial.remove(exponent_considered)
            n=len(polynomial)
        else:
            a=a+1
    return polynomial

def writhe_number(knot_unperturbed):
    w=0
    intersections=check_intersections(knot_unperturbed)
    for i in range(len(intersections)):
        a=0
        while a < len(knot_unperturbed):
            strand_considered=knot_unperturbed[a]
            intersection_considered=strand_considered[-1]
            if intersection_considered[0]==intersections[i]:
                if intersection_considered[1]==-1:
                    w=w+1
                if intersection_considered[1]==1:
                    w=w-1
            a=a+1
    return w

def bracket_polynomial_no_removal(knot_unperturbed):
    bracket=list(['+',0,knot_unperturbed])
    intersections=check_intersections(knot_unperturbed)
    length_intersections=len(intersections)
    while length_intersections>0:
        intersection=intersections[0]
        new_bracket=list()
        for i in range(2,len(bracket),3):
            exponent=bracket[i-1]
            knot=bracket[i]
            knot_A=split_intersection_A(knot,intersection)
            knot_A_inverse=split_intersection_A_inverse(knot,intersection)
            new_bracket.append('+')
            new_bracket.append(exponent+1)
            new_bracket.append(knot_A)
            new_bracket.append('+')
            new_bracket.append(exponent-1)
            new_bracket.append(knot_A_inverse)
        bracket=new_bracket
        intersections.remove(intersection)
        length_intersections=len(intersections)
    bracket=compile_bracket(bracket)
    return bracket

def remove_knots(bracket_unperturbed):
    bracket=copy.deepcopy(bracket_unperturbed)
    a=0
    while a < len(bracket):
        bracket_considered=bracket[a]
        knot_considered=copy.deepcopy(bracket_considered[2])
        if len(knot_considered)> 1:
            bracket.remove(bracket_considered)
            delete=knot_considered.pop(0)
            if bracket_considered[0]=='+':
                sign='-'
            else:
                sign='+'
            exponent=bracket_considered[1]
            exponent1=exponent+2
            exponent2=exponent-2
            new_bracket_1=[sign,exponent1,knot_considered]
            new_bracket_2=[sign,exponent2,knot_considered]
            bracket.insert(a,new_bracket_1)
            bracket.insert(a+1,new_bracket_2)
        else:
            a=a+1
    return bracket

def X (knot_unperturbed,bracket):
    knot=copy.deepcopy(knot_unperturbed)
    writhe=writhe_number(knot)
    if writhe%2==0:
        check=1
    else:
        check=-1
    writhe=-3*writhe
    for i in range(len(bracket)):
        bracket_considered=bracket[i]
        bracket_considered[0]=bracket_considered[0]*check
        bracket_considered[1]=bracket_considered[1]+writhe
    return bracket

def convert_to_jones(bracket_unperturbed):
    bracket=copy.deepcopy(bracket_unperturbed)
    for i in range(len(bracket)):
        bracket_considered=bracket[i]
        bracket_considered[1]=-bracket_considered[1]/4
    return bracket

def complete_polynomial_bracket ():
    knot_unperturbed=collect_parametrized_knot()
    bracket=copy.deepcopy(knot_unperturbed)
    bracket=bracket_polynomial_no_removal(bracket)
    bracket=remove_knots(bracket)
    bracket=compile_coefficients(bracket)
    bracket=X(knot_unperturbed,bracket)
    bracket=convert_to_jones(bracket)
    return bracket

jones_polynomial=complete_polynomial_bracket()
print("\033[1;37;48m \n")
print()
print()
print('jones polynomial is', jones_polynomial)
print()
print()

#knot_test=list([[[1,1],[2,0],[3,-1]],[[2,1],[3,0],[1,-1]],[[3,1],[1,0],[2,-1]]])
#jonespolynomial=complete_polynomial_bracket(knot_test)
#print(jonespolynomial)

#knot_test_2=list([[[1,-1],[2,0],[3,1]],[[2,-1],[3,0],[1,1]],[[3,-1],[1,0],[2,1]]])
#jonespolynomial2=complete_polynomial_bracket(knot_test_2)
#print(jonespolynomial2)