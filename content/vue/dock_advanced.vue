<Dock :model="items">
    <template #item="{ item }">
        <a v-tooltip.top="item.label" href="#" class="p-dock-item-link" @click="onDockItemClick($event, item)">
            <img :alt="item.label" :src="item.icon" style="width: 100%" />
        </a>
    </template>
</Dock>