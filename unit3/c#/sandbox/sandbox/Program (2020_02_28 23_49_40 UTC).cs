using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sandbox
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] x = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            int result = SumOfEvens(x);
            Console.WriteLine("The sum of even integers is: " + result);
            Console.ReadLine();
        }

        static void dictTest()
        {
            List<Dictionary<int, string>> list_of_things = new List<Dictionary<int, string>>()
            {
                new Dictionary<int, string> ()
                { {0 , "lion"} },

                new Dictionary<int, string> ()
                {{1, "wolf"} },

                new Dictionary<int, string> ()
                {{2, "dragons"} },

                new Dictionary<int, string> ()
                {{3,"deer"} },

                new Dictionary<int, string> ()
                {{4, "eagle"} },

                new Dictionary<int, string> ()
                {{5, "squid"} },

                new Dictionary<int, string> ()
                {{6, "fish"} }
            };

            foreach (Dictionary<int, string> item in list_of_things)
            {

                foreach (KeyValuePair<int, string> kvp in item)
                {
                    //Console.WriteLine(kvp.Key + "\t" + kvp.Value);

                    //string example = kvp.ToString().ToUpper();

                    //Console.WriteLine(example);
                    /** if (item.Values.Contains("lion"))
                    {
                        Console.WriteLine("ROAR!");
                    } **/
                }

            }

            string invalid = "0123456789 ";
            Console.WriteLine("enter a string");
            string input = Console.ReadLine();

            if (input.Contains(invalid))
            {
                Console.WriteLine("Error");
            }
            else
            {
                Console.WriteLine("correct!");
            }
        }

        private static int SumOfEvens(int[] x)

        {
            int result = 0;
            foreach (int i in x)

                if (i % 2 == 0)
                {
                    result += i;
                }
            return result;
        }


    }
}
