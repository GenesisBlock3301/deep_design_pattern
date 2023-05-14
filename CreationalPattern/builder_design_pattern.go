package main

import "fmt"

//In this example, each method returns the HouseBuilder interface, which allows us to
//chain the next method call to it. This makes it easier to read and understand the
//construction process for the House object, since all the code is contained on a single line.

type HouseBuilder interface {
	SetWall(material string) HouseBuilder
	SetRoof(material string) HouseBuilder
	SetDoor(material string, color string) HouseBuilder
	SetWindow(material string, size string) HouseBuilder
	Build() House
}

type House struct {
	Walls  string
	Roof   string
	Door   Door
	Window Window
}

type Door struct {
	Material string
	Color    string
}

type Window struct {
	Material string
	Size     string
}

// Con-create Builder

type ModernHouseBuilder struct {
	House House
}

func (m *ModernHouseBuilder) SetWall(material string) HouseBuilder {
	m.House.Walls = material
	return m
}
func (m *ModernHouseBuilder) SetRoof(material string) HouseBuilder {
	m.House.Roof = material
	return m
}

func (m *ModernHouseBuilder) SetDoor(material string, color string) HouseBuilder {
	m.House.Door.Material = material
	m.House.Door.Color = color
	return m
}

func (m *ModernHouseBuilder) SetWindow(material string, size string) HouseBuilder {
	m.House.Window.Material = material
	m.House.Window.Size = size
	return m
}

func (m *ModernHouseBuilder) Build() House {
	return m.House
}
func main() {
	builder := &ModernHouseBuilder{}
	house := builder.
		SetWall("Brick").
		SetRoof("Tile").
		SetDoor("Wood", "Brown").
		SetWindow("Glass", "Large").
		Build()
	fmt.Println(house)
}
