# spore-city-planner

To end the debates once and for all about which city layout is the best in *Spore*, I present my brute-force, so-called algorithm. Thanks to the relatively small size of towns, it doesn't take much time to compute. There are various approaches online, including genetic algorithms ([example #1](http://www.drx.dk/sporecitylayout.php), [example #2](https://github.com/makspll/spore-best-city-layout)), but I think using a genetic algorithm here is a bit like using a cannon to kill a sparrow, given the simplicity of the task, not to mention that it can sometimes get stuck in a local optimum.

I haven't created a user interface yet, so you'll need to open the script manually in your IDE. There's a boolean parameter named `allow_sad` that, surprisingly, determines whether negative happiness is permitted in the town. This might be more profitable if you use loyalty and happiness boosters on your planets. Six different layouts (`colony` and `homeworld_1` to `homeworld_5`) are encoded as graph edges, representing each city configuration. All possible town developments are then sorted by, in order of decreasing priority:
- productivity (descending);
- building cost (ascending);
- happiness (descending);
- population (descending; useful for the Civilization stage).

Of course, you can define your own sorting order and parameters.

Using my script, it becomes clear that there's more than one optimal layout. While configurations shared on [Reddit](https://www.reddit.com/r/Spore/comments/gu5unm/in_responce_to_ranger_jackal_heres_the_actual/) or the [Spore Wiki](https://spore.fandom.com/wiki/City#Colonies) are indeed optimal, they're incorrect in claiming theirs is **the** optimal solution rather than **one of** the optimal solutions 🤓.
