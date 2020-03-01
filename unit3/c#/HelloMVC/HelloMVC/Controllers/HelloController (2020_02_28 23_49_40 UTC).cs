using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace HelloMVC.Controllers
{
    public class HelloController : Controller
    {
        static int counter = 0;
        // GET: /<controller>/
        //can also do name equals something
        [HttpGet]
        public IActionResult Index(string name)
        {
            /**if (string.IsNullOrEmpty(name))
            {
                name = "World";
            } 
            action='/Hello/Display'

             **/

            string html = "<form method='post' action='/Hello/Display'>" +
                "<select name='languages' >"+
                "<option value='eng' selected='selected'>English</option>" +
                "<option value = 'fren'>French</option>" +
                "<option value ='span'>Spanish</option>" +
                "<option value='telg'>Telugu</option>" +
                "<option value='hebr'>Hebrew</option>"+
                "<input type = 'text' name = 'name' id = 'name'/>" +
                "<input type='submit' value = 'Greet me!'/>" +
                "</form>";

            //return Content(html, "text/html");
            //return Redirect("/Hello/Goodbye");
            return Content(html, "text/html");
        }
        // Hello/Goodbye
        //alter route to : /Hello/Aloha
        //[Route("Hello/Aloha")] - reroutes app
        //string name = "World"

        [Route("/Hello/Display")]
        [HttpPost]
        //paramteteres need to match form name
        public IActionResult Display (string name, string languages)
        {
            //counter++;
            if (Request.Cookies.Equals(null))
            {

                Response.Cookies.Append("count", counter.ToString());
            }
            else
            {
                counter++;
                //cookies[name] = ++;
                
                Response.Cookies.Append("count", counter.ToString());
            }
            
            string msg = CreateMessage(name, languages) + "<p>You have visted this site " + 
                counter + " times </p>";
            return Content(string.Format("<h1>{0}</h1>", msg), "text/html");
            //return Content(string.Format("Hello {0}!", name), "text/html");
        }

        public static string CreateMessage (string name, string lang)
        {
            string msg = "";

            if (lang == "eng")
            {
                msg = "Hello " + name + "!";
            }
            else if (lang == "span")
            {
                msg = "Hola " + name + "!";
            }

            else if (lang == "fren")
            {
                msg = "Bonjour " + name + "!";
            }

            else if (lang == "telg")
            {
                msg = "Namathe " + name + "!";
            }

            else if (lang == "hebr")
            {
                msg = "Shalom " + name + "!";
            }

            return msg;
            //will return Hola name if lang == span
        }

        //Handle requests to /Hello/name (url segment)
        //[Route("/Hello/{name}")]
        public IActionResult Index2(string name) //same as /Hello?name=name
        {
            return Content(string.Format("Hello {0}!", name), "text/html");
        }

        public IActionResult Goodbye ()
        {
            return Content("Goodbye");
        }
    }
}
