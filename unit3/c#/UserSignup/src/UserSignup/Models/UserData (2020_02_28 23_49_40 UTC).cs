using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace UserSignup.Models
{
    public class UserData
    {
        static private List<User> users = new List<User>();
        //TODO 2: instantiate a few new users in code here and add them to your users list
        //then write methods to add users to your list, return all users and return a user by UserId

        public static void AddUser (User u)
        {
            users.Add(u);
        }

        public static List<User> GetUsers ()
        {
            return users;
        }

        public static User GetById(int UserId)
        {
            //lambda
            User user = users.Find(u => u.UserId == UserId);
            return user;

            /** foreach(User u in user) {
             * 
             * if(u.UserId == UserId) {
             * 
             * return u;
             * }
             * }
             * 
             * return would be required */
             
        }
    }
}
