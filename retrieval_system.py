import graphlab

print 'Loading data...'
database = graphlab.SFrame('querydata')
print 'Loading model...'
knn_model = graphlab.load_model('my_model')
print 'Done.\n'
again = True
while again:
    print 'Please enter the id starting with NCT.'
    print 'For example: entering NCT01130285'
    query_number = raw_input('Please enter: ')
    # print query_number
    query_item = database[database['Identifier'] == query_number]
    ans = knn_model.query(query_item)
    print "The following is the information of retrieved studies:"
    print ''
    
    for i in range(1, 5):
        study_id = ans['reference_label'][i]
        study = database[database['Identifier'] == study_id]
        print "No. %d:" % (i), study_id
        print 'Title:', study['Title'][0]
        print 'Summary:'
        print study['Summary'][0]
        print 'Condition:', study['Condition'][0]
        print 'Intervention:', study['Intervention_name'][0]
        print 'Status:', study['Status'][0]
        print ''

    repeat = raw_input("Press 'r' to restart another search or 'q' to quit the program. \> ")
    if repeat == 'r':
        again = True
    elif repeat == 'q':
        again = False
        exit() 