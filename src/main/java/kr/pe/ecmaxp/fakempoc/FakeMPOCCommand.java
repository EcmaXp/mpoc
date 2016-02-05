package kr.pe.ecmaxp.fakempoc;

import java.util.List;

import net.minecraft.command.ICommand;
import net.minecraft.command.ICommandSender;

public class FakeMPOCCommand implements ICommand {
	public FakeMPOCCommand() {
		
	}
	
	@Override
	public int compareTo(Object o) {
		return 0;
	}

	@Override
	public String getCommandName() {
		return "asd";
	}

	@Override
	public String getCommandUsage(ICommandSender p_71518_1_) {
		return "/asd [test]";
	}

	@Override
	public List<String> getCommandAliases() {
		return null;
	}

	@Override
	public void processCommand(ICommandSender p_71515_1_, String[] p_71515_2_) {
		FakeMPOCDebug.handle(p_71515_1_, p_71515_2_);
	}

	@Override
	public boolean canCommandSenderUseCommand(ICommandSender p_71519_1_) {
		// check for debug..
		return true;
	}

	@Override
	public List<String> addTabCompletionOptions(ICommandSender p_71516_1_, String[] p_71516_2_) {
		return null;
	}

	@Override
	public boolean isUsernameIndex(String[] p_82358_1_, int p_82358_2_) {
		return false;
	}
}
