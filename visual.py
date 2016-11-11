import sfml as sf

class Visual:
    def __init__(self, world):
        self.window = sf.RenderWindow(sf.VideoMode(1024, 600), "Emergency Facility Location Problem")
        self.facilities = []
        self.world = []

        font = sf.Font.from_file("font.ttf")
        for x in xrange(world.shape[0]):
            for y in xrange(world.shape[1]):
                demand = sf.Text(str(world[x, y]), font)
                demand.character_size = 10
                demand.color = sf.Color.BLUE
                demand.position = (x * 20, y * 20)
                area = sf.RectangleShape()
                area.size = (20, 20)
                area.fill_color = sf.Color(0, 0, 0, world[x, y]/10*255)
                area.position = (x * 20, y * 20)
                self.world.append((area, demand))

        self.stats = sf.Text( "Iterations :  0000000000000000000 \nFitness    : 0000000000000000000", font)
        self.stats.character_size = 14
        self.stats.color = sf.Color.MAGENTA
        self.stats.position = (self.window.size.x - self.stats.local_bounds.width, 0)

    def __del__(self):
        self.window.close()

    def update(self, particles, stats):
        self.window.clear(sf.Color.WHITE)

        # Render map
        for area in self.world:
            self.window.draw(area[0])
            self.window.draw(area[1])

        count = 0
        for p in particles:
            for f in range(p.position.shape[0]/2):
                if count >= len(self.facilities):
                    self.facilities.append(sf.CircleShape())

                self.facilities[count].radius = 3
                self.facilities[count].fill_color = sf.Color.RED
                self.facilities[count].position = (10 + p.position[f * 2 + 0] * 20, 10 + p.position[f * 2 + 1] * 20)
                self.window.draw(self.facilities[count])

        self.stats.string = stats
        self.window.draw(self.stats)

        self.window.display()
