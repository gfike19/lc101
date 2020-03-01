﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace UserSignup.ViewModels
{
    public class User
    {
        public string Username { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public int UserId { get; set; }
        public string FavColor { get; internal set; }

        private static int nextId = 1;

        public User()
        {
            UserId = nextId;
            nextId++;
        }
    }
}
