Pokemom Data Analysis
================
Yi Chen

## A Glance at the Dataset

Below is our dataset, where the `fileName` columns are strings that
correspond to the file names of the images, the `name` column contains
the name of each Pokemon, and the `type1` and `type2` column provide
their classifications.

``` r
data %>%
  head()
```

    ##   fileName          name type1  type2
    ## 1        1     Bulbasaur Grass Poison
    ## 2        2       Ivysaur Grass Poison
    ## 3        3      Venosaur Grass Poison
    ## 4   3-mega Mega Venosaur Grass Poison
    ## 5        4    Charmander  Fire       
    ## 6        5    Charmeleon  Fire

``` r
count1 <- data %>%
  count(type1) %>%
  arrange(desc(n))
count1
```

    ## # A tibble: 18 x 2
    ##    type1        n
    ##    <fct>    <int>
    ##  1 Water      121
    ##  2 Normal      87
    ##  3 Bug         72
    ##  4 Grass       68
    ##  5 Psychic     56
    ##  6 Fire        53
    ##  7 Electric    44
    ##  8 Rock        40
    ##  9 Dragon      35
    ## 10 Ground      32
    ## 11 Poison      30
    ## 12 Fighting    29
    ## 13 Steel       28
    ## 14 Ice         27
    ## 15 Dark        26
    ## 16 Ghost       26
    ## 17 Flying      23
    ## 18 Fairy       14

We can see above that there is a rather large variation in the number of
images we have of each Pokemon type, we expect this to have some
negative effects on our model’s ability to scale.

Some Pokemons have secondary types:

``` r
count2 <- data %>%
  count(type2) %>%
  arrange(desc(n)) %>%
  slice(-1)
count2
```

    ## # A tibble: 18 x 2
    ##    type2        n
    ##    <fct>    <int>
    ##  1 Flying      80
    ##  2 Ground      36
    ##  3 Poison      36
    ##  4 Psychic     31
    ##  5 Grass       26
    ##  6 Dark        25
    ##  7 Normal      25
    ##  8 Fighting    23
    ##  9 Steel       22
    ## 10 Fairy       18
    ## 11 Rock        18
    ## 12 Ghost       17
    ## 13 Dragon      15
    ## 14 Fire        12
    ## 15 Ice         11
    ## 16 Water       10
    ## 17 Electric     6
    ## 18 Bug          3

``` r
sum(count1$n)
```

    ## [1] 811

``` r
sum(count2$n)
```

    ## [1] 414

Calculating the sums, we see that the secondary type is missing for many
Pokemon types. Therefore, we will be using `type1` to label our training
data for the model.
