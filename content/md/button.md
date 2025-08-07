# Button

Button is an extension to standard input element with icons and theming.

## Import [#](https://primevue.org/button/#import)

```

import Button from 'primevue/button';


```

## Basic [#](https://primevue.org/button/#basic)

Text to display on a button is defined with the *label* property.

Submit

```

<Button label="Submit" />


```

## Icons [#](https://primevue.org/button/#icons)

Icon of a button is specified with *icon* property and position is configured using *iconPos* attribute.

ProfileSave

SearchUpdate

```

<Button icon="pi pi-home" aria-label="Save" />
<Button label="Profile" icon="pi pi-user" />
<Button label="Save" icon="pi pi-check" iconPos="right" />
<Button label="Search" icon="pi pi-search" iconPos="top" />
<Button label="Update" icon="pi pi-refresh" iconPos="bottom" />


```

## Loading [#](https://primevue.org/button/#loading)

Busy state is controlled with the *loading* property.

Search

```

<Button type="button" label="Search" icon="pi pi-search" :loading="loading" @click="load" />


```

## Link [#](https://primevue.org/button/#link)

The button element can be displayed as a link element visually when the *link* property is present. If you need to customize the rendering, use the *as* to change the element or *asChild* for advanced templating.

Link[External](https://vuejs.org/)[Router](https://primevue.org/)

```

<Button label="Link" variant="link" />
<Button as="a" label="External" href="https://vuejs.org/" target="_blank" rel="noopener" />
<Button asChild v-slot="slotProps">
    <RouterLink to="/" :class="slotProps.class">Router</RouterLink>
</Button>


```

## Severity [#](https://primevue.org/button/#severity)

The *severity* property defines the variant of a button.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" />
<Button label="Secondary" severity="secondary" />
<Button label="Success" severity="success" />
<Button label="Info" severity="info" />
<Button label="Warn" severity="warn" />
<Button label="Help" severity="help" />
<Button label="Danger" severity="danger" />
<Button label="Contrast" severity="contrast" />


```

## Disabled [#](https://primevue.org/button/#disabled)

When *disabled* is present, the element cannot be used.

Submit

```

<Button label="Submit" disabled />


```

## Raised [#](https://primevue.org/button/#raised)

Raised buttons display a shadow to indicate elevation.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" raised />
<Button label="Secondary" severity="secondary" raised />
<Button label="Success" severity="success" raised />
<Button label="Info" severity="info" raised />
<Button label="Warn" severity="warn" raised />
<Button label="Help" severity="help" raised />
<Button label="Danger" severity="danger" raised />
<Button label="Contrast" severity="contrast" raised />


```

## Rounded [#](https://primevue.org/button/#rounded)

Rounded buttons have a circular border radius.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" rounded />
<Button label="Secondary" severity="secondary" rounded />
<Button label="Success" severity="success" rounded />
<Button label="Info" severity="info" rounded />
<Button label="Warn" severity="warn" rounded />
<Button label="Help" severity="help" rounded />
<Button label="Danger" severity="danger" rounded />
<Button label="Contrast" severity="contrast" rounded />


```

## Text [#](https://primevue.org/button/#text)

Text buttons are displayed as textual elements.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" variant="text" />
<Button label="Secondary" severity="secondary" variant="text" />
<Button label="Success" severity="success" variant="text" />
<Button label="Info" severity="info" variant="text" />
<Button label="Warn" severity="warn" variant="text" />
<Button label="Help" severity="help" variant="text" />
<Button label="Danger" severity="danger" variant="text" />
<Button label="Contrast" severity="contrast" variant="text" />


```

## Raised Text [#](https://primevue.org/button/#raisedtext)

Text buttons can be displayed elevated with the *raised* option.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" variant="text" raised />
<Button label="Secondary" severity="secondary" variant="text" raised />
<Button label="Success" severity="success" variant="text" raised />
<Button label="Info" severity="info" variant="text" raised />
<Button label="Warn" severity="warn" variant="text" raised />
<Button label="Help" severity="help" variant="text" raised />
<Button label="Danger" severity="danger" variant="text" raised />
<Button label="Contrast" severity="contrast" variant="text" raised />


```

## Outlined [#](https://primevue.org/button/#outlined)

Outlined buttons display a border without a transparent background.

PrimarySecondarySuccessInfoWarnHelpDangerContrast

```

<Button label="Primary" variant="outlined" />
<Button label="Secondary" severity="secondary" variant="outlined" />
<Button label="Success" severity="success" variant="outlined" />
<Button label="Info" severity="info" variant="outlined" />
<Button label="Warn" severity="warn" variant="outlined" />
<Button label="Help" severity="help" variant="outlined" />
<Button label="Danger" severity="danger" variant="outlined" />
<Button label="Contrast" severity="contrast" variant="outlined" />


```

## Icon Only [#](https://primevue.org/button/#icononly)

Buttons can have icons without labels.

SmallNormalLarge

```

<Button icon="pi pi-check" aria-label="Filter" />
<Button icon="pi pi-bookmark" severity="secondary" aria-label="Bookmark" />
<Button icon="pi pi-search" severity="success" aria-label="Search" />
<Button icon="pi pi-user" severity="info" aria-label="User" />
<Button icon="pi pi-bell" severity="warn" aria-label="Notification" />
<Button icon="pi pi-heart" severity="help" aria-label="Favorite" />
<Button icon="pi pi-times" severity="danger" aria-label="Cancel" />
<Button icon="pi pi-star" severity="contrast" aria-label="Star" />

<Button icon="pi pi-check" rounded aria-label="Filter" />
<Button icon="pi pi-bookmark" severity="secondary" rounded aria-label="Bookmark" />
<Button icon="pi pi-search" severity="success" rounded aria-label="Search" />
<Button icon="pi pi-user" severity="info" rounded aria-label="User" />
<Button icon="pi pi-bell" severity="warn" rounded aria-label="Notification" />
<Button icon="pi pi-heart" severity="help" rounded aria-label="Favorite" />
<Button icon="pi pi-times" severity="danger" rounded aria-label="Cancel" />
<Button icon="pi pi-star" severity="contrast" rounded aria-label="Star" />

<Button icon="pi pi-check" rounded variant="outlined" aria-label="Filter" />
<Button icon="pi pi-bookmark" severity="secondary" rounded variant="outlined" aria-label="Bookmark" />
<Button icon="pi pi-search" severity="success" rounded variant="outlined" aria-label="Search" />
<Button icon="pi pi-user" severity="info" rounded variant="outlined" aria-label="User" />
<Button icon="pi pi-bell" severity="warn" rounded variant="outlined" aria-label="Notification" />
<Button icon="pi pi-heart" severity="help" rounded variant="outlined" aria-label="Favorite" />
<Button icon="pi pi-times" severity="danger" rounded variant="outlined" aria-label="Cancel" />
<Button icon="pi pi-star" severity="contrast" rounded variant="outlined" aria-label="Star" />

<Button icon="pi pi-check" variant="text" raised rounded aria-label="Filter" />
<Button icon="pi pi-bookmark" severity="secondary" variant="text" raised rounded aria-label="Bookmark" />
<Button icon="pi pi-search" severity="success" variant="text" raised rounded aria-label="Search" />
<Button icon="pi pi-user" severity="info" variant="text" raised rounded aria-label="User" />
<Button icon="pi pi-bell" severity="warn" variant="text" raised rounded aria-label="Notification" />
<Button icon="pi pi-heart" severity="help" variant="text" raised rounded aria-label="Favorite" />
<Button icon="pi pi-times" severity="danger" variant="text" raised rounded aria-label="Cancel" />
<Button icon="pi pi-star" severity="contrast" variant="text" raised rounded aria-label="Star" />

<Button icon="pi pi-check" variant="text" rounded aria-label="Filter" />
<Button icon="pi pi-bookmark" severity="secondary" variant="text" rounded aria-label="Bookmark" />
<Button icon="pi pi-search" severity="success" variant="text" rounded aria-label="Search" />
<Button icon="pi pi-user" severity="info" variant="text" rounded aria-label="User" />
<Button icon="pi pi-bell" severity="warn" variant="text" rounded aria-label="Notification" />
<Button icon="pi pi-heart" severity="help" variant="text" rounded aria-label="Favorite" />
<Button icon="pi pi-times" severity="danger" variant="text" rounded aria-label="Cancel" />
<Button icon="pi pi-star" severity="contrast" variant="text" rounded aria-label="Star" />


```

## Badge [#](https://primevue.org/button/#badge)

Buttons have built-in badge support with *badge* and *badgeSeverity* properties.

Emails2Messages2

```

<Button type="button" label="Emails" badge="2" />
<Button type="button" label="Messages" icon="pi pi-users" badge="2" badgeSeverity="contrast" variant="outlined"  />


```

## Button Group [#](https://primevue.org/button/#buttongroup)

Multiple buttons are grouped when wrapped inside an element with *ButtonGroup* component.

SaveDeleteCancel

```

<ButtonGroup>
    <Button label="Save" icon="pi pi-check" />
    <Button label="Delete" icon="pi pi-trash" />
    <Button label="Cancel" icon="pi pi-times" />
</ButtonGroup>


```

## Sizes [#](https://primevue.org/button/#sizes)

Button provides *small* and *large* sizes as alternatives to the base.

SmallNormalLarge

```

<Button label="Small" icon="pi pi-check" size="small" />
<Button label="Normal" icon="pi pi-check" />
<Button label="Large" icon="pi pi-check" size="large" />


```

## Template [#](https://primevue.org/button/#template)

Custom content inside a button is defined as children.

```

<Button variant="outlined" class="!border-2">
    <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="..." fill="var(--p-primary-color)" />
        <path d="..." fill="var(--p-text-color)" />
    </svg>
</Button>


```

## Headless [#](https://primevue.org/button/#headless)

Headless mode is enabled by adding the *asChild* property and defining your own UI element with the available bindings.

SIGN UP

```

<Button v-slot="slotProps" asChild>
    <button
        v-bind="slotProps.a11yAttrs"
        class="rounded-lg bg-gradient-to-br from-primary-400 to-primary-700 active:from-primary-700 active:to-primary-900 text-white border-none px-6 py-3 font-bold hover:ring-2 cursor-pointer ring-offset-2 ring-offset-surface-0 dark:ring-offset-surface-900 ring-primary transition-all"
    >
        SIGN UP
    </button>
</Button>


```

## Accessibility [#](https://primevue.org/button/#accessibility)

### Screen Reader

Button component renders a native button element that implicitly includes any passed prop. Text to describe the button is defined with the *aria-label* prop, if not present *label* prop is used as the value. If the button is icon only or custom templating is used, it is recommended to use *aria-label* so that screen readers would be able to read the element properly.

```

<Button icon="pi pi-check" aria-label="Submit" />

<Button icon="pi pi-check" label="Submit" />

<Button class="youtube p-0" aria-label="Youtube">
    <i class="pi pi-youtube px-2"></i>
    <span class="px-4">Youtube</span>
</Button>


```

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the button. |
| *enter* | Activates the button. |
| *space* | Activates the button. |