# Avatar

Avatar represents people using icons, labels and images.

## Import [#](https://primevue.org/avatar/#import)

```

import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';   //Optional for grouping


```

## Label [#](https://primevue.org/avatar/#label)

A letter Avatar is defined with the *label* property.

##### Label

P

V

U

##### Circle

P

V

U

##### Badge

U

4

```

<Avatar label="P" class="mr-2" size="xlarge" />
<Avatar label="V" class="mr-2" size="large" style="background-color: #ece9fc; color: #2a1261" />
<Avatar label="U" class="mr-2" style="background-color: #dee9fc; color: #1a2551" />

<Avatar label="P" class="mr-2" size="xlarge" shape="circle" />
<Avatar label="V" class="mr-2" size="large" style="background-color: #ece9fc; color: #2a1261" shape="circle" />
<Avatar label="U" class="mr-2" style="background-color: #dee9fc; color: #1a2551" shape="circle" />

<OverlayBadge value="4" severity="danger" class="inline-flex">
    <Avatar label="U" size="xlarge" />
</OverlayBadge>


```

## Icon [#](https://primevue.org/avatar/#icon)

A font icon is displayed as an Avatar with the *icon* property.

##### Icon

##### Circle

##### Badge

4

```

<Avatar icon="pi pi-user" class="mr-2" size="xlarge" />
<Avatar icon="pi pi-user" class="mr-2" size="large" style="background-color: #ece9fc; color: #2a1261" />
<Avatar icon="pi pi-user" style="background-color: #dee9fc; color: #1a2551" />

<Avatar icon="pi pi-user" class="mr-2" size="xlarge" shape="circle" />
<Avatar icon="pi pi-user" class="mr-2" size="large" style="background-color: #ece9fc; color: #2a1261" shape="circle" />
<Avatar icon="pi pi-user" style="background-color: #dee9fc; color: #1a2551" shape="circle" />

<OverlayBadge value="4" severity="danger" class="inline-flex">
    <Avatar icon="pi pi-user" size="xlarge" />
</OverlayBadge>


```

## Image [#](https://primevue.org/avatar/#image)

Use the *image* property to display an image as an Avatar.

##### Image

##### Badge

4

##### Gravatar

```

<Avatar image="/images/avatar/amyelsner.png" class="mr-2" size="xlarge" shape="circle" />
<Avatar image="/images/avatar/asiyajavayant.png" class="mr-2" size="large" shape="circle" />
<Avatar image="/images/avatar/onyamalimba.png" shape="circle" />

<OverlayBadge value="4" severity="danger" class="inline-flex">
    <Avatar class="p-overlay-badge" image="https://primefaces.org/cdn/primevue/images/organization/walter.jpg" size="xlarge" />
</OverlayBadge>

<Avatar image="https://www.gravatar.com/avatar/05dfd4b41340d09cae045235eb0893c3?d=mp" class="flex items-center justify-center mr-2" size="xlarge" />


```

## AvatarGroup [#](https://primevue.org/avatar/#avatargroup)

Grouping is available by wrapping multiple Avatar components inside an AvatarGroup.

+2

```

<AvatarGroup>
    <Avatar image="/images/avatar/amyelsner.png" shape="circle" />
    <Avatar image="/images/avatar/asiyajavayant.png" shape="circle" />
    <Avatar image="/images/avatar/onyamalimba.png" shape="circle" />
    <Avatar image="/images/avatar/ionibowcher.png" shape="circle" />
    <Avatar image="/images/avatar/xuxuefeng.png" shape="circle" />
    <Avatar label="+2" shape="circle" />
</AvatarGroup>


```

## Accessibility [#](https://primevue.org/avatar/#accessibility)

### Screen Reader

Avatar does not include any roles and attributes by default. Any attribute is passed to the root element so you may add a role like *img* along with *aria-labelledby* or *aria-label* to describe the component. In case avatars need to be tabbable, *tabindex* can be added as well to implement custom key handlers.

### Keyboard Support

Component does not include any interactive elements.