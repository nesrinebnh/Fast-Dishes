package main

import (
	"backend/database"
	"backend/routes"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func main() {
	//Connecting to the database
	database.Connect()

	app := fiber.New()

	//Must be added because of http request only
	app.Use(cors.New(cors.Config{
		AllowCredentials: true, //this will allow the frontend to get the cookie
	}))

	routes.Setup(app)

	app.Listen(":8000")
}
