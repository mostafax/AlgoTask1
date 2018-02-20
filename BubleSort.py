def bubble_sort(list):

    list1 = list

    for i in range(0,len(list1)):

        for j in range(0,len(list1)):

            if(list1[i] < list1[j]):

                temp = list1[i]

                list1[i] = list1[j]

                list1[j] = temp



    return (list1)