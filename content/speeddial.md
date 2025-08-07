# Speed Dial

When pressed, a floating action button can display multiple primary actions that can be performed on a page.

## Import [#](https://primevue.org/speeddial/#import)

```

import SpeedDial from 'primevue/speeddial';


```

## Linear [#](https://primevue.org/speeddial/#linear)

SpeedDial items are defined with the *model* property based on MenuModel API. Default orientation of the items is linear and *direction* property is used to define the position of the items related to the button.

```

<SpeedDial :model="items" direction="up" style="position: absolute; left: calc(50% - 2rem); bottom: 0" />
<SpeedDial :model="items" direction="down" style="position: absolute; left: calc(50% - 2rem); top: 0" />
<SpeedDial :model="items" direction="left" style="position: absolute; top: calc(50% - 2rem); right: 0" />
<SpeedDial :model="items" direction="right" style="position: absolute; top: calc(50% - 2rem); left: 0" />


```

## Circle [#](https://primevue.org/speeddial/#circle)

Items can be displayed around the button when *type* is set to *circle*. Additional *radius* property defines the radius of the circle.

```

<SpeedDial :model="items" :radius="80" type="circle" :style="{ position: 'absolute' }" :buttonProps="{ severity: 'warn', rounded: true }" />


```

## Semi Circle [#](https://primevue.org/speeddial/#semi-circle)

When *type* is defined as *semi-circle*, items are displayed in a half-circle around the button.

```

<SpeedDial :model="items" :radius="80" type="semi-circle" direction="up" style="position: absolute; left: calc(50% - 2rem); bottom: 0" />
<SpeedDial :model="items" :radius="80" type="semi-circle" direction="down" style="position: absolute; left: calc(50% - 2rem); top: 0" />
<SpeedDial :model="items" :radius="80" type="semi-circle" direction="left" style="position: absolute; top: calc(50% - 2rem); right: 0" />
<SpeedDial :model="items" :radius="80" type="semi-circle" direction="right" style="position: absolute; top: calc(50% - 2rem); left: 0" />


```

## Quarter Circle [#](https://primevue.org/speeddial/#quarter-circle)

Setting *type* as *quarter-circle* displays the items at one of four corners of a button based on the *direction*.

```

<SpeedDial :model="items" :radius="120" type="quarter-circle" direction="up-left" :style="{ position: 'absolute', right: 0, bottom: 0 }" />
<SpeedDial :model="items" :radius="120" type="quarter-circle" direction="up-right" :style="{ position: 'absolute', left: 0, bottom: 0 }" />
<SpeedDial :model="items" :radius="120" type="quarter-circle" direction="down-left" :style="{ position: 'absolute', right: 0, top: 0 }" />
<SpeedDial :model="items" :radius="120" type="quarter-circle" direction="down-right" :style="{ position: 'absolute', left: 0, top: 0 }" />


```

## Tooltip [#](https://primevue.org/speeddial/#tooltip)

Items display a tooltip on hover when a standalone [Tooltip](https://primevue.org/tooltip/) is present with a target that matches the items.

```

<SpeedDial :model="items" direction="up" :style="{ position: 'absolute', right: 0, bottom: 0 }" :buttonProps="{ severity: 'help', rounded: true }" :tooltipOptions="{ position: 'left' }" />
<SpeedDial :model="items" direction="up" :style="{ position: 'absolute', left: 0, bottom: 0 }" :buttonProps="{ severity: 'danger', rounded: true }" :tooltipOptions="{ position: 'right' }" />


```

## Mask [#](https://primevue.org/speeddial/#mask)

Adding *mask* property displays a modal layer behind the popup items.

```

<SpeedDial :model="items" direction="up" mask :style="{ position: 'absolute', right: '1rem', bottom: '1rem' }" />


```

## Template [#](https://primevue.org/speeddial/#template)

SpeedDial offers item customization with the *item* template that receives the menuitem instance from the model as a parameter. The button has its own *button* template, additional slot named *icon* is provided to embed icon content for default button.

* Add
* Update
* Delete
* Upload
* Website

```

<SpeedDial :model="items" direction="up" :transitionDelay="80" :style="{ position: 'absolute' }" pt:menuitem="m-2">
    <template #button="{ toggleCallback }">
        <Button variant="outlined" class="border" @click="toggleCallback">
            <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="..." fill="var(--p-primary-color)" />
                <path d="..." fill="var(--p-text-color)" />
            </svg>
        </Button>
    </template>
    <template #item="{ item, toggleCallback }">
        <div class="flex flex-col items-center justify-between gap-2 p-2 border rounded border-surface-200 dark:border-surface-700 w-20 cursor-pointer" @click="toggleCallback">
            <span :class="item.icon" />
            <span>
                {{ item.label }}
            </span>
        </div>
    </template>
</SpeedDial>


```

## Accessibility [#](https://primevue.org/speeddial/#accessibility)

### Screen Reader

SpeedDial component renders a native button element that implicitly includes any passed prop. Text to describe the button can be defined with the *aria-labelledby* or *aria-label* props. Addititonally the button includes includes *aria-haspopup*, *aria-expanded* for states along with *aria-controls* to define the relation between the popup and the button.

The popup overlay uses *menu* role on the list and each action item has a *menuitem* role with an *aria-label* as the menuitem label. The id of the menu refers to the *aria-controls* of the button.

```

<SpeedDial aria-label="Options" />


```

### Menu Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Toggles the visibility of the menu. |
| *space* | Toggles the visibility of the menu. |
| *down arrow* | Opens the menu and moves focus to the first item. |
| *up arrow* | Opens the menu and moves focus to the last item. |
| *right arrow* | Opens the menu and moves focus to the last item. |
| *left arrow* | Opens the menu and moves focus to the first item. |
| *escape* | Closes the menu. |

### Menu Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Actives the menuitem, closes the menu and sets focus on the menu button. |
| *space* | Actives the menuitem, closes the menu and sets focus on the menu button. |
| *escape* | Closes the menu and sets focus on the menu button. |
| *arrow keys* | Navigates between the menu items. |
| *home* | Moves focus to the first item. |
| *end* | Moves focus to the last item. |