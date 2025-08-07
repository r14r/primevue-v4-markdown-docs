# Badge

Badge is a small status indicator for another element.

## Import [#](https://primevue.org/badge/#import)

```

// import as component
import Badge from 'primevue/badge';
import OverlayBadge from 'primevue/overlaybadge';


```

## Basic [#](https://primevue.org/badge/#basic)

Content to display is defined with the *value* property or the default slot.

210

```

<Badge value="2"></Badge>
<Badge>10</Badge>


```

## Severity [#](https://primevue.org/badge/#severity)

Severity defines the variant of a badge.

2684935

```

<Badge value="2"></Badge>
<Badge value="6" severity="secondary"></Badge>
<Badge value="8" severity="success"></Badge>
<Badge value="4" severity="info"></Badge>
<Badge value="9" severity="warn"></Badge>
<Badge value="3" severity="danger"></Badge>
<Badge value="5" severity="contrast"></Badge>


```

## Size [#](https://primevue.org/badge/#size)

Use the *size* property to customize the dimensions of a Badge.

8642

```

<Badge value="8" size="xlarge" severity="success"></Badge>
<Badge value="6" size="large" severity="warn"></Badge>
<Badge value="4" severity="info"></Badge>
<Badge value="2" size="small"></Badge>


```

## Overlay [#](https://primevue.org/badge/#overlay)

A badge can be added to any element by encapsulating the content with the *OverlayBadge* component.

2

4

```

<OverlayBadge value="2">
    <i class="pi pi-bell" style="font-size: 2rem" />
</OverlayBadge>
<OverlayBadge value="4" severity="danger">
    <i class="pi pi-calendar" style="font-size: 2rem" />
</OverlayBadge>
<OverlayBadge severity="danger">
    <i class="pi pi-envelope" style="font-size: 2rem" />
</OverlayBadge>


```

## Button [#](https://primevue.org/badge/#button)

Buttons have built-in support for badges to display a badge inline.

Notifications2Inbox2

```

<Button type="button" label="Notifications" icon="pi pi-bell" badge="2" />
<Button type="button" label="Inbox" icon="pi pi-inbox" badge="2" badgeSeverity="contrast" variant="outlined" />


```

## Accessibility [#](https://primevue.org/badge/#accessibility)

### Screen Reader

Badge does not include any roles and attributes by default, any attribute is passed to the root element so aria roles and attributes can be added if required. If the badges are dynamic, *aria-live* may be utilized as well. In case badges need to be tabbable, *tabindex* can be added to implement custom key handlers.

### Keyboard Support

Component does not include any interactive elements.