package com.example.shadowmod;

import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

@Mod("shadowmod")
public class ShadowMod {
    
    public static final String MOD_ID = "shadowmod";
    
    // deferred registers for items and blocks
    private static final DeferredRegister<Item> ITEMS = 
        DeferredRegister.create(ForgeRegistries.ITEMS, MOD_ID);
    private static final DeferredRegister<Block> BLOCKS = 
        DeferredRegister.create(ForgeRegistries.BLOCKS, MOD_ID);
    
    // custom items
    public static final RegistryObject<Item> SUPER_PICKAXE = ITEMS.register("super_pickaxe",
        () -> new Item(new Item.Properties().durability(2031)));
    
    public static final RegistryObject<Item> SHADOW_INGOT = ITEMS.register("shadow_ingot",
        () -> new Item(new Item.Properties()));
    
    // custom block
    public static final RegistryObject<Block> SHADOW_ORE = BLOCKS.register("shadow_ore",
        () -> new Block(Block.Properties.ofFullCopy(Blocks.STONE)));
    
    public ShadowMod() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
        
        ITEMS.register(modEventBus);
        BLOCKS.register(modEventBus);
        
        modEventBus.addListener(this::commonSetup);
        
        MinecraftForge.EVENT_BUS.register(this);
    }
    
    private void commonSetup(final FMLCommonSetupEvent event) {
        System.out.println("shadow mod loaded!");
    }
    
    // register block items
    @SubscribeEvent
    public void buildCreativeModeTabContents(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == CreativeModeTabs.TOOLS_AND_UTILITIES) {
            event.accept(SUPER_PICKAXE);
        }
        if (event.getTabKey() == CreativeModeTabs.INGREDIENTS) {
            event.accept(SHADOW_INGOT);
        }
    }
}
