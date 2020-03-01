using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Metadata;

namespace CheeseMVC.Migrations
{
    public partial class ModifyCheeseMenuKey : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_CheeseMenus",
                table: "CheeseMenus");

            migrationBuilder.DropColumn(
                name: "ID",
                table: "CheeseMenus");

            migrationBuilder.AddPrimaryKey(
                name: "PK_CheeseMenus",
                table: "CheeseMenus",
                columns: new[] { "CheeseID", "MenuID" });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_CheeseMenus",
                table: "CheeseMenus");

            migrationBuilder.AddColumn<int>(
                name: "ID",
                table: "CheeseMenus",
                nullable: false,
                defaultValue: 0)
                .Annotation("SqlServer:ValueGenerationStrategy", SqlServerValueGenerationStrategy.IdentityColumn);

            migrationBuilder.AddPrimaryKey(
                name: "PK_CheeseMenus",
                table: "CheeseMenus",
                column: "ID");
        }
    }
}
