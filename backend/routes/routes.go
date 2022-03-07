package routes

import (
	"backend/controlers"

	"github.com/gofiber/fiber/v2"
)

func Setup(app *fiber.App) {
	app.Get("/api/recipes/fetch", controlers.GetRecipes)
	app.Post("/api/recipes/add", controlers.AddRecipes)
}
