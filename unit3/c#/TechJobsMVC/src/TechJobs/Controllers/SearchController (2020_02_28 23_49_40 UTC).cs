using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using TechJobs.Models;

namespace TechJobs.Controllers
{
    public class SearchController : Controller
    {
        public IActionResult Index()
        {
            ViewBag.columns = ListController.columnChoices;
            ViewBag.title = "Search";
            return View();
        }
        
        public IActionResult Results (string searchType, string searchTerm)
        {
            List<Dictionary<string, string>> Jobs;
            if (searchType.Equals("all"))
            {
                Jobs = JobData.FindByValue(searchTerm);
            }
            else
            {
                Jobs = JobData.FindByColumnAndValue(searchType, searchTerm);
            }

            ViewBag.columns = ListController.columnChoices;
            ViewBag.jobs = Jobs;
            return View("Index");
        }
    }
}
