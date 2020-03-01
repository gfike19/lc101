using System;
using System.Collections.Generic;
using System.Text;

namespace Cities.Comparers
{
    class CompoundComparer : IComparer<City>
    {
        public List<IComparer<City>> Comparers = new List<IComparer<City>>();

        public int Compare (City x, City y)
        {
            //gets how many Comparers are in the list
            int size = Comparers.Count;
            //will act as iterator
            int i = 0;
            //we want this to be zero as that indicates all comparisons are done
            int compareResults = 0;

            //as long as i isn't as big as size AND compareResults isn't correct, keep going
            //both conidtions need to be met
           while (i < size && compareResults == 0)
            {
                //set compareResults to output of Comparer that the iterator is on
                compareResults = Comparers[i].Compare(x, y);
                //increment iterator
                i++;
            }

    
            return compareResults;
        }
    }
}
