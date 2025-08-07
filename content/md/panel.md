# Panel

Panel is a grouping component providing with content toggle feature.

## Import [#](https://primevue.org/panel/#import)

```

import Panel from 'primevue/panel';


```

## Basic [#](https://primevue.org/panel/#basic)

A simple Panel is created with a *header* property along with the content as children.

Header

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<Panel header="Header">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Panel>


```

## Toggleable [#](https://primevue.org/panel/#toggleable)

Content of the panel can be expanded and collapsed using *toggleable* option.

Header

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<Panel header="Header" toggleable>
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Panel>


```

## Template [#](https://primevue.org/panel/#template)

Header, icons and footer sections of the panel are customizable via templating.

Amy Elsner

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Updated 2 hours ago

```

<Panel toggleable>
    <template #header>
        <div class="flex items-center gap-2">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold">Amy Elsner</span>
        </div>
    </template>
    <template #footer>
        <div class="flex flex-wrap items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <Button icon="pi pi-user" rounded text></Button>
                <Button icon="pi pi-bookmark" severity="secondary" rounded text></Button>
            </div>
            <span class="text-surface-500 dark:text-surface-400">Updated 2 hours ago</span>
        </div>
    </template>
    <template #icons>
        <Button icon="pi pi-cog" severity="secondary" rounded text @click="toggle" />
        <Menu ref="menu" id="config_menu" :model="items" popup />
    </template>
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Panel>


```

## Accessibility [#](https://primevue.org/panel/#accessibility)

### Screen Reader

Toggleable panels use a content toggle button at the header that has *aria-controls* to define the id of the content section along with *aria-expanded* for the visibility state. The value to read the button defaults to the value of the *header* property and can be customized by defining an *aria-label* or *aria-labelledby* via the *toggleButtonProps* property.

The content uses *region*, defines an id that matches the *aria-controls* of the content toggle button and *aria-labelledby* referring to the id of the header.

### Content Toggle Button Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous the focusable element in the page tab sequence. |
| *enter* | Toggles the visibility of the content. |
| *space* | Toggles the visibility of the content. |