void dump_current_locations(Bomber *bombers, int bomber_count, Bomb *bombs, int bomb_count, Obstacle *obstacles, int obstacle_count, int map_width, int map_height) {
    printf("initial %d %d %d %d\n", map_width, map_height, obstacle_count, bomber_count);
    for (int i = 0; i < obstacle_count; i++) {
        if (!obstacles[i].destroyed)
            printf("map obstacle %d %d %d %d\n",i, obstacles[i].x, obstacles[i].y, obstacles[i].durability);
    }
    for (int i = 0; i < bomber_count; i++) {
        if (bombers[i].alive)
            printf("map bomber %d %d %d\n", bombers[i].pid, bombers[i].x, bombers[i].y);
    }
    for (int i = 0; i < bomb_count; i++) {
        if (bombs[i].planted && !bombs[i].exploded)
            printf("map bomb %d %d %d \n", bombs[i].pid, bombs[i].x, bombs[i].y);
    }
}

int main() {


    // other code

    bomber_response = poll(...);

    while (1) {
        
        if bomber_response > 0{

            dump_current_locations(...);

            // other code

        }
        // other code
    }

    // other code

}