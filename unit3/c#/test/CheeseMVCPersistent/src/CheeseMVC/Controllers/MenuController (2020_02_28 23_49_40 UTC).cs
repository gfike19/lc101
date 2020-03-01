using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using CheeseMVC.Data;
using CheeseMVC.Models;
using Microsoft.EntityFrameworkCore;
using CheeseMVC.ViewModels;

namespace CheeseMVC.Controllers
{
    public class MenuController : Controller
    {
        private CheeseDbContext context;

        public MenuController(CheeseDbContext dbContext)
        {
            context = dbContext;
        }

        public IActionResult Index()
        {
            //IList<Menu> menus = context.Menus.Include(c => c.ID).ToList();
            List<Menu> menus = context.Menus.ToList();

            return View(menus);
        }

        public IActionResult Add()
        {
            AddMenuViewModel addMenuViewModel = new AddMenuViewModel();
            return View(addMenuViewModel);
        }

        [HttpPost]
        public IActionResult Add(AddMenuViewModel addMenuViewModel)
        {
            if (ModelState.IsValid)
            {
                Menu newMenu = new Menu
                {
                    Name = addMenuViewModel.Name
                };

                context.Menus.Add(newMenu);
                context.SaveChanges();

                return Redirect("/Menu/ViewMenu/" + newMenu.ID);
            }

            return View(addMenuViewModel);
        }

        public IActionResult ViewMenu(int id)
        {
            Menu menu = context.Menus.Single(c => id == c.ID);
            List<CheeseMenu> items = context.CheeseMenus.Include(item => item.Cheese).Where(cm => cm.MenuID == id).ToList();
            ViewMenuViewModel viewMenuViewModel = new ViewMenuViewModel
            {
                Menu = menu,
                Items = items
            };
            return View(viewMenuViewModel);
        }

        public IActionResult AddItem(int id)
        {
            Menu menu = context.Menus.Single(c => id == c.ID);
            List<Cheese> items = context.Cheeses.ToList();
            AddMenuItemViewModel addMenuItemViewModel = new AddMenuItemViewModel(menu, items);
            return View(addMenuItemViewModel);
        }

        [HttpPost]
        public IActionResult AddItem(AddMenuItemViewModel addMenuItemViewModel)
        {
            if (ModelState.IsValid)
            {

                IList<CheeseMenu> existingItems = context.CheeseMenus
                .Where(cm => cm.CheeseID == addMenuItemViewModel.CheeseID)
                .Where(cm => cm.MenuID == addMenuItemViewModel.MenuID).ToList();

                if (existingItems.Count == 0)
                {
                    CheeseMenu newCheeseMenu = new CheeseMenu
                    {
                        MenuID = addMenuItemViewModel.MenuID,
                        CheeseID = addMenuItemViewModel.CheeseID
                    };

                    context.CheeseMenus.Add(newCheeseMenu);
                    context.SaveChanges();

                    return Redirect("/Menu/ViewMenu/" + newCheeseMenu.MenuID);
                }
            }

            return View(addMenuItemViewModel);
        }
    }
}
