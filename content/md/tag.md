# Tag

Tag component is used to categorize content.

## Import [#](https://primevue.org/tag/#import)

```

import Tag from 'primevue/tag';


```

## Basic [#](https://primevue.org/tag/#basic)

Label of the tag is defined with the *value* property.

New

```

<Tag value="New"></Tag>


```

## Severity [#](https://primevue.org/tag/#severity)

Severity defines the variant of a tag.

PrimarySecondarySuccessInfoWarnDangerContrast

```

<Tag value="Primary"></Tag>
<Tag severity="secondary" value="Secondary"></Tag>
<Tag severity="success" value="Success"></Tag>
<Tag severity="info" value="Info"></Tag>
<Tag severity="warn" value="Warn"></Tag>
<Tag severity="danger" value="Danger"></Tag>
<Tag severity="contrast" value="Contrast"></Tag>


```

## Pill [#](https://primevue.org/tag/#pill)

Enabling *rounded*, displays a tag as a pill.

PrimarySecondarySuccessInfoWarnDangerContrast

```

<Tag value="Primary" rounded></Tag>
<Tag severity="secondary" value="Secondary" rounded></Tag>
<Tag severity="success" value="Success" rounded></Tag>
<Tag severity="info" value="Info" rounded></Tag>
<Tag severity="warn" value="Warn" rounded></Tag>
<Tag severity="danger" value="Danger" rounded></Tag>
<Tag severity="contrast" value="Contrast" rounded></Tag>


```

## Icon [#](https://primevue.org/tag/#icons)

A font icon next to the value can be displayed with the *icon* property.

PrimarySecondarySuccessInfoWarnDangerContrast

```

<Tag icon="pi pi-user" value="Primary"></Tag>
<Tag icon="pi pi-search" severity="secondary" value="Secondary"></Tag>
<Tag icon="pi pi-check" severity="success" value="Success"></Tag>
<Tag icon="pi pi-info-circle" severity="info" value="Info"></Tag>
<Tag icon="pi pi-exclamation-triangle" severity="warn" value="Warn"></Tag>
<Tag icon="pi pi-times" severity="danger" value="Danger"></Tag>
<Tag icon="pi pi-cog" severity="contrast" value="Contrast"></Tag>


```

## Template [#](https://primevue.org/tag/#template)

Children of the component are passed as the content for templating.

Italy

```

<Tag style="border: 2px solid var(--border-color); background: transparent; color: var(--text-color)">
    <div class="flex items-center gap-2 px-1">
        <img alt="Country" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" class="flag flag-it" style="width: 18px" />
        <span class="text-base">Italy</span>
    </div>
</Tag>


```

## Accessibility [#](https://primevue.org/tag/#accessibility)

### Screen Reader

Tag does not include any roles and attributes by default, any attribute is passed to the root element so aria roles and attributes can be added if required. If the tags are dynamic, *aria-live* may be utilized as well. In case badges need to be tabbable, *tabindex* can be added to implement custom key handlers.

### Keyboard Support

Component does not include any interactive elements.