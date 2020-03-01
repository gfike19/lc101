using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Restaraunt
{
    class MenuItem
    {
        //TODO this is incorrect as setting it up this way doesn't allow you to access these variables when you create instances of them
        /** private string name { get; }
        private string descr { get; }
        private double price { get; set; }
        private DateTime date = DateTime.Now;
        private string cat; **/

        private readonly string name;
        private readonly string descr;
        private double price;
        private string cat;

        private DateTime date = DateTime.Now;

        public MenuItem(string name, string descr, double price, string cat)
        {
            this.name = name;
            this.descr = descr;
            this.price = price;
            this.cat = cat;
        }

        public string GetName()
        {
            return name;
        }

        public string GetDescr()
        {
            return descr;
        }

        public double GetPrice()
        {
            return price;
        }

        public void SetPrice(double value)
        {
            price = value;
        }

        public  string GetCat ()
        {
            return this.cat;
        }

        public string ToString()
        {
            return this.cat + "\n" + this.name + "\n" + this.descr + "\n" + this.price + "\n" + this.date;
        }

        //how do we determine if an item is new
        public string CheckDate ()
        {
            DateTime current = DateTime.Today;
            if (date.CompareTo(current) < 0)
            {
                return "new";
            }
            else
                return "old";
        }

    }
}
