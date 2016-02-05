package kr.pe.ecmaxp.fakempoc;

import net.minecraft.command.ICommandSender;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.item.ItemStack;
import net.minecraft.nbt.NBTTagCompound;
import net.minecraft.util.ChatComponentText;
import net.minecraft.world.World;

public class FakeMPOCDebug {
	public static void handle(ICommandSender sender, String[] args) {
		// DEBUG ONLY
		System.out.println("***** START *****");

		try {
			String result = command(sender, args);
			System.out.println(result);
			sender.addChatMessage(new ChatComponentText(result));
		} catch (Exception e) {
			System.out.println("***** ERROR *****");
			e.printStackTrace();
			sender.addChatMessage(new ChatComponentText("has Error"));
			return;
		}
		
		System.out.println("***** DONE *****");
		sender.addChatMessage(new ChatComponentText("done."));
	}
	
	public static String command(ICommandSender sender, String[] args) {
		// do debug stuff in here!
		if (sender.getCommandSenderName().equals("Rcon")) {
			return "require player";
		}
		
		World world = sender.getEntityWorld();
		EntityPlayer player = world.getPlayerEntityByName(sender.getCommandSenderName());
		String cmd = args.length >= 1? args[0]: "";
		if (cmd.equals("py")) {
			return "??";
		} else if (cmd.equals("ss")) {
			ItemStack item = player.getHeldItem();
			return item.stackTagCompound.toString();
		} else if (cmd.equals("as")) {			
			ItemStack item = player.getHeldItem();
			NBTTagCompound nbt = item.stackTagCompound;
			nbt = nbt.getCompoundTag("oc:data");
			byte[] code = nbt.getByteArray("oc:eeprom");
			return new String(code).replace("\n", "\r\n");
		} else if (cmd.equals("bios")) {
			String namespace = "oc:";
			String eeprom = "done";
			String userdata = "";
			
		    NBTTagCompound nbt = new NBTTagCompound();
    	    nbt.setString(namespace + "label", "Python BIOS");
    	    nbt.setByteArray(namespace + "eeprom", eeprom.getBytes());
    	    nbt.setByteArray(namespace + "userdata", userdata.getBytes());
    	    nbt.setBoolean(namespace + "readonly", false);

    	    NBTTagCompound stackNbt = new NBTTagCompound();
    	    stackNbt.setTag(namespace + "data", nbt);

    	    ItemStack stack = player.getHeldItem();
    	    stack.setTagCompound(stackNbt);
    	    return "write OK";
		} else if (cmd.equals("bios")) {
			String namespace = "oc:";
			String eeprom = "done";
			String userdata = "";
			
		    NBTTagCompound nbt = new NBTTagCompound();
    	    nbt.setString(namespace + "label", "Python BIOS");
    	    nbt.setByteArray(namespace + "eeprom", eeprom.getBytes());
    	    nbt.setByteArray(namespace + "userdata", userdata.getBytes());
    	    nbt.setBoolean(namespace + "readonly", false);

    	    NBTTagCompound stackNbt = new NBTTagCompound();
    	    stackNbt.setTag(namespace + "data", nbt);

    	    ItemStack stack = player.getHeldItem();
    	    stack.setTagCompound(stackNbt);
    	    return "BIOS write OK";
		} else if (cmd.equals("")) {
			return FakeMPOC.INSTANCE.toString();
		}
		
		return "hello world: " + cmd;
	}
}
