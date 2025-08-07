<PanelMenu :model="items">
    <template #item="{ item }">
        <a v-ripple class="flex items-center px-4 py-2 cursor-pointer group">
            <span :class="[item.icon, 'text-primary group-hover:text-inherit']" />
            <span :class="['ml-2', { 'font-semibold': item.items }]">{{ item.label }}</span>
            <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
            <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
        </a>
    </template>
</PanelMenu>