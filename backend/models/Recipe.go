package models

type Recipe struct {
	Id          int    `json:"id"`
	Title       string `json:"title"`
	Description string `json:"description"`
	ImageUrl    string `json:"url"`
	Level       string `json:"level"`
	Duration    string `json:"duration"`
}
