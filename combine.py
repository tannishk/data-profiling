import distribution as db
import split as sp
import primarykey as pk
import muloutlier as ml
import matplotlib.pyplot
get_ipython().magic(u'matplotlib inline')
def result(a):
    print ' The complete summary with Graph '
    j = {}
    for i in a:

        j[i] = db.distri(a, i)
        print i,'is',j[i]
        if(a[i].dtype=='object'):
            print 'Its unique occurance is'
            print sp.uniqueoccur(a, i)
            ##print ' Type of',i,'is:'
            sp.type1(a,i)
        if(a[i].dtype=='int64' or a[i].dtype=='float64'):
            sp.desc(a,i)
            if(j[i]=='discrete'):
                print ' ITs discrete so you may not want to display this '
        print '***************************'


        if((a[i].dtype=='int64' or a[i].dtype=='float64') and j[i]=='continous' ):
            print ' Ouliers for individual columns if numeric and continours'
            db.outliers1(a,i)
    print ' Primary Key analysis '
    print pk.primarykey(a)
    print ' '
    print ' '

    print ' '
    print ' '
    print 'Final outliers'
    ml.mulout(a)  ## one class SVM
    print ' '
    print ' '

    print ' '
    print ' '