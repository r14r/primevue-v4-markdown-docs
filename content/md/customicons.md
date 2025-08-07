# Custom Icons

PrimeVue components can be used with any icon library using the templating features.

## Material [#](https://primevue.org/customicons/#material)

[Material icons](https://fonts.google.com/icons) is the official icon library based on Google Material Design.

```

<Select>
    <template #dropdownicon>
        <span class="material-icons">arrow_drop_down</span>
    </template>
</Select>


```

## FontAwesome [#](https://primevue.org/customicons/#fontawesome)

[Font Awesome](https://fontawesome.com/) is a popular icon library with a wide range of icons.

```

<Select>
    <template #dropdownicon>
        <i class="fa-light fa-chevron-down"></i>
    </template>
</Select>


```

## SVG [#](https://primevue.org/customicons/#svg)

Inline SVGs are embedded inside the dom.

```

<Select>
    <template #dropdownicon>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g id="chevron-down">
                <path d="M12,15.25a.74.74,0,0,1-.53-.22l-5-5A.75.75,0,0,1,7.53,9L12,13.44,16.47,9A.75.75,0,0,1,17.53,10l-5,5A.74.74,0,0,1,12,15.25Z"/>
            </g>
        </svg>
    </template>
</Select>


```

## Image [#](https://primevue.org/customicons/#image)

Any type of image can be used as an icon.

```

<Select>
    <template #dropdownicon>
        <img alt="dropdown icon" src="/assets/icons/arrow_down.png">
    </template>
</Select>


```

## Video Tutorial [#](https://primevue.org/customicons/#video)

A video tutorial to demonstrate how to customize icons.