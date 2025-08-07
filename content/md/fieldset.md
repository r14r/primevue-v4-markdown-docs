# Fieldset

Fieldset is a grouping component with a content toggle feature.

## Import [#](https://primevue.org/fieldset/#import)

```

import Fieldset from 'primevue/fieldset';


```

## Basic [#](https://primevue.org/fieldset/#basic)

A simple Fieldset is created with a *legend* property along with the content as children.

Header

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<Fieldset legend="Header">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Fieldset>


```

## Toggleable [#](https://primevue.org/fieldset/#toggleable)

Content of the fieldset can be expanded and collapsed when *toggleable* option is enabled.

Header

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<Fieldset legend="Header" :toggleable="true">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Fieldset>


```

## Template [#](https://primevue.org/fieldset/#template)

Legend section can be customized with custom content using templating.

Amy Elsner

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<Fieldset>
    <template #legend>
        <div class="flex items-center pl-2">
            <Avatar image="/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold p-2">Amy Elsner</span>
        </div>
    </template>
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Fieldset>


```

## Accessibility [#](https://primevue.org/fieldset/#accessibility)

### Screen Reader

Fieldset component uses the semantic *fieldset* element. When toggleable option is enabled, a button element is included inside the *legend* element, this button has *aria-controls* to define the id of the content section along with *aria-expanded* for the visibility state. The value to read the button defaults to the value of the *legend* property and can be customized by defining an *aria-label* or *aria-labelledby* via the *toggleButtonProps* property.

The content uses *region*, defines an id that matches the *aria-controls* of the content toggle button and *aria-labelledby* referring to the id of the header.

###### Content Toggle Button Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus to the next the focusable element in the page tab sequence. |
| *shift* + *tab* | Moves focus to the previous the focusable element in the page tab sequence. |
| *enter* | Toggles the visibility of the content. |
| *space* | Toggles the visibility of the content. |