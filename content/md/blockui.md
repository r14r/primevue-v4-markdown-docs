# BlockUI

BlockUI can either block other components or the whole page.

## Import [#](https://primevue.org/blockui/#import)

```

import BlockUI from 'primevue/blockui';


```

## Basic [#](https://primevue.org/blockui/#basic)

The element to block should be placed as a child of BlockUI and *blocked* property is required to control the state.

BlockUnblock

Basic

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

<div class="mb-4">
    <Button label="Block" @click="blocked = true" class="mr-2"></Button>
    <Button label="Unblock" @click="blocked = false"></Button>
</div>
<BlockUI :blocked="blocked">
    <Panel header="Basic">
        <p class="m-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </Panel>
</BlockUI>


```

## Document [#](https://primevue.org/blockui/#document)

Enabling *fullScreen* property controls the document.

Block

```

<BlockUI :blocked="blocked" fullScreen />
<Button label="Block" @click="blocked = true" />


```

## Accessibility [#](https://primevue.org/blockui/#accessibility)

### Screen Reader

BlockUI manages *aria-busy* state attribute when the UI gets blocked and unblocked. Any valid attribute is passed to the root element so additional attributes like *role* and *aria-live* can be used to define live regions.

### Keyboard Support

Component does not include any interactive elements.