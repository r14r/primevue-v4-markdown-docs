# SplitButton

SplitButton groups a set of commands in an overlay with a default command.

## Import [#](https://primevue.org/splitbutton/#import)

```

import SplitButton from 'primevue/splitbutton';


```

## Basic [#](https://primevue.org/splitbutton/#basic)

SplitButton has a default command button and a collection of additional options defined by the *model* property.

Save

```

<SplitButton label="Save" @click="save" :model="items" />


```

## Icons [#](https://primevue.org/splitbutton/#icons)

The buttons and menuitems have support to display icons.

Save

```

<SplitButton label="Save" icon="pi pi-check" dropdownIcon="pi pi-cog" @click="save" :model="items" />


```

## Nested [#](https://primevue.org/splitbutton/#nested)

Multi-level menus are supported with a nested menu hierarchy.

Save

```

<SplitButton label="Save" @click="save" :model="items" />


```

## Severity [#](https://primevue.org/splitbutton/#severity)

The *severity* property defines the variant of a button.

Save

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="danger"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" severity="contrast"></SplitButton>


```

## Disabled [#](https://primevue.org/splitbutton/#disabled)

When *disabled* is present, the element cannot be edited and focused.

Save

```

<SplitButton label="Save" @click="save" :model="items" disabled />


```

## Raised [#](https://primevue.org/splitbutton/#raised)

Raised buttons display a shadow to indicate elevation.

Save

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save" raised></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="danger"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised severity="contrast"></SplitButton>


```

## Rounded [#](https://primevue.org/splitbutton/#rounded)

Rounded buttons have a circular border radius.

Save

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save" rounded></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="danger"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" rounded severity="contrast"></SplitButton>


```

## Text [#](https://primevue.org/splitbutton/#text)

Text buttons are displayed as textual elements.

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save" text></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" text severity="danger"></SplitButton>


```

## Raised Text [#](https://primevue.org/splitbutton/#raisedtext)

Text buttons can be displayed as raised as well for elevation.

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save" raised text></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" raised text severity="danger"></SplitButton>


```

## Outlined [#](https://primevue.org/splitbutton/#outlined)

Outlined buttons display a border without a background initially.

Save

Save

Save

Save

Save

Save

Save

Save

```

<SplitButton label="Save" :model="items" @click="save" outlined></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="secondary"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="success"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="info"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="warn"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="help"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="danger"></SplitButton>
<SplitButton label="Save" :model="items" @click="save" outlined severity="contrast"></SplitButton>


```

## Sizes [#](https://primevue.org/splitbutton/#sizes)

SplitButton provides *small* and *large* sizes as alternatives to the standard.

Save

Save

Save

```

<SplitButton label="Save" :model="items" icon="pi pi-plus" size="small"></SplitButton>
<SplitButton label="Save" :model="items" icon="pi pi-plus"></SplitButton>
<SplitButton label="Save" :model="items" icon="pi pi-plus" size="large"></SplitButton>


```

## Template [#](https://primevue.org/splitbutton/#template)

Custom content inside a button is defined as children.

PrimeVue

```

<SplitButton :model="items" @click="save" severity="contrast">
    <span class="flex items-center font-bold">
        <img alt="logo" src="https://primefaces.org/cdn/primevue/images/logo.svg" style="height: 1rem; margin-right: 0.5rem" />
        <span>PrimeVue</span>
    </span>
</SplitButton>


```

## Accessibility [#](https://primevue.org/splitbutton/#accessibility)

### Screen Reader

SplitButton component renders two native button elements, main button uses the label property to define *aria-label* by default which can be customized with *buttonProps*. Dropdown button requires an explicit definition to describe it using *menuButtonProps* option and also includes *aria-haspopup*, *aria-expanded* for states along with *aria-controls* to define the relation between the popup and the button.

The popup overlay uses *menu* role on the list and each action item has a *menuitem* role with an *aria-label* as the menuitem label. The id of the menu refers to the *aria-controls* of the dropdown button.

```

<SplitButton :buttonProps="{'aria-label': 'Default Action'}" :menuButtonProps="{'aria-label': 'More Options'}" />


```

### Main Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | Activates the button. |
| *space* | Activates the button. |

### Menu Button Keyboard Support

| Key | Function |
| --- | --- |
| *enter**space**down arrow**up arrow* | Opens the menu and moves focus to the first item. |

### Menu Keyboard Support

| Key | Function |
| --- | --- |
| *enter* | If menuitem has a submenu, opens the submenu otherwise activates the menuitem and closes all open overlays. |
| *space* | If menuitem has a submenu, opens the submenu otherwise activates the menuitem and closes all open overlays. |
| *escape* | If focus is inside a popup submenu, closes the submenu and moves focus to the root item of the closed submenu. |
| *down arrow* | Moves focus to the next menuitem within the submenu. |
| *up arrow* | Moves focus to the previous menuitem within the submenu. |
| *alt* + *up arrow* | Closes the popup, then moves focus to the target element. |
| *right arrow* | In nested mode if option is closed, opens the option otherwise moves focus to the first child option. |
| *left arrow* | In nested mode if option is open, closes the option otherwise moves focus to the parent option. |
| *home* | Moves focus to the first menuitem within the submenu. |
| *end* | Moves focus to the last menuitem within the submenu. |
| *any printable character* | Moves focus to the menuitem whose label starts with the characters being typed. |