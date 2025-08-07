# TieredMenu

TieredMenu displays submenus in nested overlays.

## Import [#](https://primevue.org/tieredmenu/#import)

```

import TieredMenu from 'primevue/tieredmenu';


```

## Basic [#](https://primevue.org/tieredmenu/#basic)

TieredMenu requires a collection of menuitems as its *model*.

* File
* Edit
* Search
* Share

```

<TieredMenu :model="items" />


```

## Popup [#](https://primevue.org/tieredmenu/#popup)

Overlay mode is enabled by adding *popup* property and calling *toggle* function of the menu ref with an event of the target.

Toggle

```

<Button type="button" label="Toggle" @click="toggle" aria-haspopup="true" aria-controls="overlay_tmenu" />
<TieredMenu ref="menu" id="overlay_tmenu" :model="items" popup />


```

## Template [#](https://primevue.org/tieredmenu/#template)

TieredMenu offers item customization with the *item* template that receives the menuitem instance from the model as a parameter.

* File
* Edit
* Search⌘+S
* Share

```

<TieredMenu :model="items">
    <template #item="{ item, props, hasSubmenu }">
        <a v-ripple class="flex items-center" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
            <i v-if="hasSubmenu" class="pi pi-angle-right ml-auto"></i>
        </a>
    </template>
</TieredMenu>


```

## Command [#](https://primevue.org/tieredmenu/#command)

The *command* property defines the callback to run when an item is activated by click or a key event.

* File
* Search
* Sync

```

<TieredMenu :model="items" />
<Toast />


```

## Router [#](https://primevue.org/tieredmenu/#router)

Items with navigation are defined with templating to be able to use a router link component, an external link or programmatic navigation.

* Router
* Programmatic
* External

```

<TieredMenu :model="items">
    <template #item="{ item, props, hasSubmenu }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <span v-if="hasSubmenu" class="pi pi-angle-right ml-auto" />
        </a>
    </template>
</TieredMenu>


```

## Accessibility [#](https://primevue.org/tieredmenu/#accessibility)

### Screen Reader

TieredMenu component uses the *menubar* role with *aria-orientation* set to "vertical" and the value to describe the menu can either be provided with *aria-labelledby* or *aria-label* props. Each list item has a *menuitem* role with *aria-label* referring to the label of the item and *aria-disabled* defined if the item is disabled. A submenu within a TieredMenu uses the *menu* role with an *aria-labelledby* defined as the id of the submenu root menuitem label. In addition, menuitems that open a submenu have *aria-haspopup* and *aria-expanded* to define the relation between the item and the submenu.

In popup mode, the component implicitly manages the *aria-expanded*, *aria-haspopup* and *aria-controls* attributes of the target element to define the relation between the target and the popup.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the next focusable item in the page tab sequence. |
| *shift* + *tab* | Add focus to the first item if focus moves in to the menu. If the focus is already within the menu, focus moves to the previous focusable item in the page tab sequence. |
| *enter* | If menuitem has a submenu, opens the submenu otherwise activates the menuitem and closes all open overlays. |
| *space* | If menuitem has a submenu, opens the submenu otherwise activates the menuitem and closes all open overlays. |
| *escape* | If focus is inside a popup submenu, closes the submenu and moves focus to the root item of the closed submenu. |
| *down arrow* | Moves focus to the next menuitem within the submenu. |
| *up arrow* | Moves focus to the previous menuitem within the submenu. |
| *alt* + *up arrow* | Closes the popup, then moves focus to the target element. |
| *right arrow* | If option is closed, opens the option otherwise moves focus to the first child option. |
| *left arrow* | If option is open, closes the option otherwise moves focus to the parent option. |
| *home* | Moves focus to the first menuitem within the submenu. |
| *end* | Moves focus to the last menuitem within the submenu. |
| *any printable character* | Moves focus to the menuitem whose label starts with the characters being typed. |