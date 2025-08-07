<Dock :model="items" :position="position">
    <template #itemicon="{ item }">
        <img v-tooltip.top="item.label" :alt="item.label" :src="item.icon" style="width: 100%" />
    </template>
</Dock>