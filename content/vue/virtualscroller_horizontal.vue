<VirtualScroller :items="items" :itemSize="50" orientation="horizontal" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px" :pt="{ content: 'flex flex-row' }">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="width: 50px; writing-mode: vertical-lr;">{{ item }}</div>
    </template>
</VirtualScroller>