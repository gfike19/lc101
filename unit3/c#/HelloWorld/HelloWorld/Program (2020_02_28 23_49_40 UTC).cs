using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            //greetings();
            //Rectangle();
            //StrFun();
            //FindEvens();
            //ListsAndStrings();
            SbExer();
        }

        static void greetings()
        {
            Console.Write("What is your name? ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello " + name + "!");
        }

        static void Rectangle()
        {
            Console.Write("Height of rectange: ");
            double ht = Double.Parse(Console.ReadLine());
            Console.Write("Length of rectangle: ");
            double wd = Double.Parse(Console.ReadLine());
            Console.WriteLine("The area is: " + ht * wd + "\n");
        }

        static void StrFun ()
        {
            string text = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'";
            text = text.ToLower();
            Console.Write("What word/s would you like to search for? ");
            string user_inp = Console.ReadLine();

            if (text.IndexOf(user_inp) >= 0)
            {
                Console.WriteLine("The string " + user_inp + " was found at position " + text.IndexOf(user_inp));
            }

            else
            {
                Console.WriteLine(user_inp + " was not found");
            }
        }

        static void FindEvens ()
        {
            List<int> nums = new List<int>();
            Random rnd = new Random();
            for (int i = 0; i < 10; i++)
            {
                int rnum = rnd.Next(0, 101);
                nums.Add(rnum);
            }

            int even_sum = 0;

            foreach (int j in nums)
            {
                Console.WriteLine("Current number is: " + j);
                if (j % 2 == 0)
                {
                    even_sum += j;
                }
            }
            Console.WriteLine("The sum of all numbers is: " + even_sum);
        }

        static void AreaOfCircle()
        {
            Console.WriteLine("What is the radius?");
            float r = float.Parse(Console.ReadLine());

            if (r < 0)
            {
                do
                {
                    Console.WriteLine("Please enter a positve number: ");
                    r = float.Parse(Console.ReadLine());
                } while (r < 0);
            }

            double area = Math.PI * (Math.Pow(r, 2));

            Console.WriteLine("Area found is: " + area);
        }

        static void ListsAndStrings ()
        {
            List<string> text = new List<string>();

            while (text.Count() < 10)
            {
                Console.WriteLine("Enter a word: ");
                text.Add(Console.ReadLine());
            }

            foreach(string str in text) {
                if (str.Length == 5)
                {
                    Console.WriteLine(str);
                }
            }
        }

        static void SbExer ()
        {
            StringBuilder sb = new StringBuilder();

            int user_inp = 0;

            while (user_inp != 7)
            {
                string menu = "1) Add \n" +
                    "2) View length \n" +
                    "3) Get capacity \n" +
                    "4) Insert \n" +
                    "5) Remove \n" +
                    "6) Replace \n" +
                    "7) Exit \n\n" +
                    "Enter a choice: ";

                Console.WriteLine(menu);
                user_inp = int.Parse(Console.ReadLine());

                if (user_inp == 1)
                {
                    Console.WriteLine("Enter some text: ");
                    string text = Console.ReadLine();

                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }
                else if (user_inp == 2)
                {
                    Console.WriteLine(sb.Length + "\n");
                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }
                else if (user_inp == 3)
                {
                    Console.WriteLine(sb.Capacity + "\n");
                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }

                else if(user_inp == 4)
                {
                    Console.WriteLine("Where do you wan to insert at? ");
                    int pos = int.Parse(Console.ReadLine());
                    Console.WriteLine("What do you want to insert? ");
                    string new_text = Console.ReadLine();

                    sb.Insert(pos, new_text);

                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }

                else if(user_inp == 5)
                {
                    Console.WriteLine("Enter the amount of characters you want to remove: ");
                    int amt = int.Parse(Console.ReadLine());

                    Console.WriteLine("At what position do you want to remove them?");
                    int pos = int.Parse(Console.ReadLine());

                    sb.Remove(pos, amt);

                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }

                else if (user_inp == 6)
                {
                    Console.WriteLine("Enter string TO be replaced: ");
                    string org = Console.ReadLine();

                    Console.WriteLine("Enter the new string: ");
                    string new_str = Console.ReadLine();

                    sb.Replace(org, new_str);

                    Console.WriteLine(menu);
                    user_inp = int.Parse(Console.ReadLine());
                }
            }
            

        }

        static void Gradebook ()
        {
            Dictionary<string, double> students =
                new Dictionary<string, double>();
            string newStudent;

            Console.WriteLine("Enter your students (or ENTER to finish):");
            do
            {
                Console.WriteLine("name: ");
                newStudent = Console.ReadLine();
                if (newStudent != "")
                {
                    // Get the student's grade
                    Console.Write("grade: ");
                    double newGrade = double.Parse(Console.ReadLine());

                    students.Add(newStudent, newGrade);
                }
            }
            while (newStudent != "");

            // Print roster
            Console.WriteLine("\nClass roster:");
            foreach (KeyValuePair<string, double> student in students)
            {
                Console.WriteLine(student.Key + " (" + student.Value + ")");
            }

            double sum = students.Values.Sum();
            double avg = sum / students.Count;
            Console.WriteLine("Average grade: " + avg);

            Console.ReadLine();
        }
    }

}
